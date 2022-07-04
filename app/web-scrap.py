from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import requests

chrome_options = Options()
chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
page = "https://www.ifood.com.br/delivery/rio-de-janeiro-rj/five-burgers-freguesia-de-jacarepagua/9d041a66-51ee-4c7a-8e2e-9524076f7bf2"
driver = webdriver.Chrome(options=chrome_options)
driver.get(page)
print(driver)
sleep(2)


def find_products(menu_items):
    products = []
    for items in menu_items:
        sleep(2)
        try:
            item_name = WebDriverWait(items, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        except:
            item_name = 'name not found'
        try:
            item_detail = WebDriverWait(items, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'dish-card__details')))
            if item_detail == '':
                item_detail = item_name
        except:
            item_detail = item_name
        try:
            item_price = WebDriverWait(items, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'dish-card__price')))
        except:
            item_price = 'price not found'
        try:
            item_image = WebDriverWait(items, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
            item_picture = item_image.get_attribute('src')
        except:
            item_picture = 'picture not found'
        product = {'item_name': item_name}
        api_product = {'item_name': item_name.text,
                       'item_detail': item_detail.text,
                       'item_price': item_price.text,
                       'item_picture': item_picture}
        products.append(product)
        if items.text == menu_items[-1].text:
            local = item_name.location
            driver.execute_script(f"window.scrollTo(0, {local['y']})")
        print(api_product)
    return products


all_products = []
all_menus = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'restaurant__fast-menu')))
local = all_menus.location
driver.execute_script(f"window.scrollTo(0, {local['y']})")
menu_items = driver.find_elements(By.CSS_SELECTOR, 'li[data-test-id="restaurant-menu-group-item"]')
print(menu_items)
while True:
    find = False
    products = find_products(menu_items)
    for product in products:
        if product['item_name'] not in [p['item_name'] for p in all_products]:
            all_products.append(product)
            find = False
        else:
            find = True
    if find:
        break
    menu_items = driver.find_elements(By.CSS_SELECTOR, 'li[data-test-id="restaurant-menu-group-item"]')

