import csv
from os import makedirs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from io import BytesIO
from PIL import Image
import requests
import datetime
import os
import time
from os.path import getsize, join
import imghdr
import os
from os.path import getsize, join


ebird_url = driver.find_element(By.XPATH, '//*[@id="Suggest-0"]'.send_keys(f'{bird_species}')

driver=webdriver.Chrome(
    executable_path='C:\\Users\\jmentore\\Documents\\Selenium Chrome Driver\\chromedriver.exe')
driver.get(ebird_url)
driver.maximize_window()

def test_search():
    ebird_url='https://ebird.org/explore'
    chromeDriver='C:\\Users\\jmentore\\Documents\\Selenium Chrome Driver\\chromedriver.exe'
    driver=webdriver.Chrome(executable_path=chromeDriver)
    driver.get(ebird_url)
    driver.maximize_window()
    element=driver.find_element_by_xpath(
        '//*[@id="Suggest-0"]').send_keys('Otus sunia')

    # select by visible text
    drop_list=select(element)
    drop_list.select_by_visible_text('Otus sunia')
    time.sleep(5000)


def search_byTaxcode(tax_code):
    taxon_code=tax_code
    ebird_url=f'https://ebird.org/species/{taxon_code}'
    chromeDriver='C:\\Users\\jmentore\\Documents\\Selenium Chrome Driver\\chromedriver.exe'
    driver=webdriver.Chrome(executable_path=chromeDriver)
    driver.get(ebird_url)
    view_all=driver.find_element(
        By.XPATH, '/html/body/div/div[7]/div/div/div[2]/div[1]/a')
    time.sleep(5)

    print("WAITING WAITING")
    view_all.click()
    print("View All Clicked")
    time.sleep(5)
    driver.quit()


def trash():
    try:
        wait=WebDriverWait(driver, 10)
        view_all=wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'Button Button--small Button--link')))
        view_all.click()
        print("View All button has been clicked")
        return True
    except (TimeoutException, NoSuchElementException) as e:
        print(str(e))
        return False
