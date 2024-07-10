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
        platform='Win32',
        webgl_vendor='Intel Inc.',
        renderer='Intel Iris OpenGL Engine',
        fix_hairline=True,
        )

data = []
page_links = []

start_url = 'https://www.amazon.com/'
page_links.append(start_url)

def get_page_links():
    driver.get(start_url)
    time.sleep(15)
    next_page_link = driver.find_element(By.CLASS_NAME, 's-pagination-next').get_attribute('href')
    while next_page_link:
        page_links.append(next_page_link)
        driver.get(next_page_link)
        next_page_link = driver.find_element(By.CLASS_NAME, 's-pagination-next').get_attribute('href')
    print(page_links)

if __name__ == '__main__':
    get_page_links()





