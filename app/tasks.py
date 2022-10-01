from __future__ import absolute_import, unicode_literals
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from iRating.celery import app
from time import sleep
import os
from .models import Product, Restaurant
from django.core.files import File
import re


def save_data(product):
    try:
        restaurant = Restaurant.objects.get(name=product['restaurant_name'])
        restaurant_id = restaurant.id
    except:
        restaurant = Restaurant.objects.create(name=product['restaurant_name'], link=product['link'])
        restaurant_id = restaurant.id

        if product['restaurant_picture'] != '':
            rest_result = urlretrieve(product['restaurant_picture'])
            restaurant.picture.save(
                os.path.basename(product['restaurant_picture']),
                File(open(rest_result[0], 'rb'))
            )
            restaurant.save()
    try:
        product_db = Product.objects.get(name=product['item_name'])
    except:
        product_db = Product.objects.create(restaurant_id=restaurant_id, name=product['item_name'],
                                            detail=product['item_detail'], price=product['item_price'])
        if product['item_picture'] != '':
            result = urlretrieve(product['item_picture'])
            product_db.picture.save(
                os.path.basename(product['item_picture']),
                File(open(result[0], 'rb'))
            )
            product_db.save()
    return True


def find_products(menu_items, driver, page):
    products = []
    for items in menu_items:
        sleep(5)
        try:
            item_name = WebDriverWait(items, 100).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        except:
            item_name = 'name not found'
        try:
            item_detail = WebDriverWait(items, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'dish-card__details')))
            if item_detail == '':
                item_detail = item_name
        except:
            item_detail = item_name
        try:
            item_price2 = WebDriverWait(items, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'dish-card__price')))
            item_price = item_price2.text
            item_price = re.sub('[^0-9,]', "", item_price)
            item_price = item_price[:5]
        except:
            item_price = ''
        try:
            item_image_link = WebDriverWait(items, 100).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
            item_image = item_image_link.get_attribute('src')
        except:
            item_image = ''
        try:
            restaurant_name = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        except:
            restaurant_name = 'name not found'
        try:
            restaurant_image_link = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'merchant-info__logo')))
            restaurant_image = restaurant_image_link.get_attribute('src')
        except:
            restaurant_image = ''
        product = {
            'item_name': item_name.text,
            'item_detail': item_detail.text,
            'item_price': item_price,
            'item_picture': item_image,
            'restaurant_name': restaurant_name.text,
            'restaurant_picture': restaurant_image,
            'link': page,
        }
        print(restaurant_name.text, product['item_name'])
        products.append(product)
        if items.text == menu_items[-1].text:
            local = item_name.location
            driver.execute_script(f"window.scrollTo(0, {local['y']})")
    return products


@app.task(name='web_scrap_ifood')
def scrap_products(page):
    page = page
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(page)
    sleep(10)
    all_products = []
    all_menus = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'restaurant__fast-menu')))
    local = all_menus.location
    driver.execute_script(f"window.scrollTo(0, {local['y']})")
    sleep(3)
    menu_items = WebDriverWait(all_menus, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li[data-test-id="restaurant-menu-group-item"]')))
    while True:
        find = False
        products = find_products(menu_items, driver, page)
        for product in products:
            if product['item_name'] not in [p['item_name'] for p in all_products]:
                all_products.append(product)
                find = False
            else:
                find = True
        if find:
            break
        menu_items = driver.find_elements(By.CSS_SELECTOR, 'li[data-test-id="restaurant-menu-group-item"]')

    for product in all_products:
        save_data(product)

