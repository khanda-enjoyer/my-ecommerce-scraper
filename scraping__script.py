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
product_links = []

start_url = 'https://www.amazon.com/s?k=over-ear+headphones&page=1&qid=1720711198&ref=sr_pg_1'
page_links.append(start_url)

def get_page_links():
    driver.get(start_url)
    time.sleep(15)
    next_page_button = driver.find_element(By.CLASS_NAME, 's-pagination-next')
    while next_page_button:
        time.sleep(3)
        next_page_link = next_page_button.get_attribute('href')
        page_links.append(next_page_link)
        try:
            driver.get(next_page_link) # type: ignore
        except:
            print('что-то пошло не так')
            return(page_links)
        next_page_button = driver.find_element(By.CLASS_NAME, 's-pagination-next')

def get_product_links():
    for page_link in page_links:
        driver.get(page_link)
        time.sleep(3)
        mainblock = driver.find_element(By.CLASS_NAME, 's-main-slot')
        product_array = mainblock.find_elements(By.CSS_SELECTOR, '.a-link-normal.s-no-outline')
        for product in product_array:
            parent = product.find_element(By.XPATH, '../../..')
            if parent.tag_name == 'span':
                continue
            else:
                product_link = product.get_attribute('href')
                product_links.append(product_link)
    return(product_links)

def get_product_info():
    for product in product_links:
        driver.get(product)
        time.sleep(3)
        mainblock = driver.find_element(By.CLASS_NAME, 'ppd')

        product_title = mainblock.find_element(By.ID, 'productTitle')
        print(product_title)

        product_price = mainblock.find_element(By.CSS_SELECTOR, '.a-section.a-spacing-none.aok-align-center.aok-relative').find_element(By.CLASS_NAME, 'aok-offscreen').text
        print(product_price)

        product_rate = mainblock.find_element(By.ID, 'acrPopover').find_element(By.CLASS_NAME, 'a-icon-alt').text
        print(product_rate)

        product_reviews = mainblock.find_element(By.ID, 'acrCustomerReviewText').text
        print(product_reviews)

        product_description = mainblock.find_element(By.ID, '.a-unordered-list.a-vertical.a-spacing-mini')
        print(product_description)

        product_images = mainblock.find_element(By.ID, 'altImages').find_elements(By.CLASS_NAME, 'imageThumbnail')
        for product_image in product_images:
            image_link = product_image.find_element(By.TAG_NAME, 'img').get_attribute('src')
            print(image_link)
if __name__ == '__main__':
    
    get_product_links()





