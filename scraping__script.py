from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument('start-maximixed')

options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=['en-US', 'en'],
        vendor='Google Inc.',
        platform='Win64',
        webgl_vendor='Intel Inc.',
        renderer='Intel Iris OpenGL Engine',
        fix_hairline=True,
        )

data = []
page_links = []

start_url = 'https://www.amazon.com/s?k=over-ear+headphones&page=2&qid=1720711198&ref=sr_pg_1'
page_links.append(start_url)

def get_page_links():
    driver.get(start_url)
    time.sleep(15)
    next_page_button = driver.find_element(By.CLASS_NAME, 's-pagination-next')
    while next_page_button != None:
        next_page_link = next_page_button.get_attribute('href')
        page_links.append(next_page_link)
        driver.get(next_page_link) # type: ignore
        next_page_button = driver.find_element(By.CLASS_NAME, 's-pagination-next')

def get_product_data():
    for page_link in page_links:
        driver.get(page_link)
        mainblock = driver.find_element(By.CLASS_NAME, 'sg-col-inner')
        product__array = mainblock.find_elements(By.CSS_SELECTOR, '.a-link-normal.s-no-outline')
        for product in product__array:
            parent = product.find_element(By.XPATH, '../../..')
            if parent.tag_name == 'span':
                continue
            
if __name__ == '__main__':
    get_page_links()





