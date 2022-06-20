from __future__ import absolute_import, unicode_literals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
import requests

chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
page = "https://www.ifood.com.br/delivery/rio-de-janeiro-rj/five-burgers-freguesia-de-jacarepagua/9d041a66-51ee-4c7a-8e2e-9524076f7bf2"
driver = webdriver.Chrome(options=chrome_options)
driver.get(page)
# highlights = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'carousel__slide')))
# for detail in highlights:
#     highlights_detail = WebDriverWait(detail, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'dish-card')))
#     highlights_detail = highlights_detail.text
menu = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'restaurant-menu-group')))

# teste aqui pra ver se o commit ta funcionando