import csv
from os import makedirs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
from io import BytesIO
from PIL import _imaging
from PIL import Image
import requests
import datetime
import os
import time
from os.path import getsize, join
import imghdr
import os
from os.path import getsize, join

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


def search_bySpecies():
    species = 'Semioptera wallacii'
    with open('request_species.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            if species == row[2]:
                #makedirs(f'testing/{row[1]}', exist_ok=True)
                makedirs(f'{row[0]}/{row[1]}/{row[2]}', exist_ok=True)
                #download_species_byOrder(row[0], row[1], row[2])
                print(row)


def NEW_download_from_CSV():
    with open('request_species.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            makedirs(f'{row[0]}/{row[1]}/{row[2]}', exist_ok=True)
            download_species_byOrder(row[0], row[1], row[2], row[3])
            time.sleep(10)


def download_species_byOrder(bird_family, bird_order, bird_species, tax_code):

    # initate web driver
    ebird_url = f'https://ebird.org/species/{tax_code}'
    chromeDriver = 'C:\\Users\\jmentore\\Documents\\Selenium Chrome Driver\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chromeDriver)
    driver.get(ebird_url)
    driver.maximize_window()
    time.sleep(3)

    # Clicks the view all link
    view_all = driver.find_element(
        By.XPATH, '/html/body/div/div[7]/div/div/div[2]/div[1]/a')
    time.sleep(5)
    view_all.click()

    ids = driver.find_elements_by_tag_name('img')
    sci_name = bird_species
    family = bird_family
    order = bird_order
    ebird_counter = 0
    file_ext = '.jpg'
    show_more = driver.find_element_by_id('show_more')

    while show_more.is_displayed():
        try:
            for ii in ids:
                download_link = ii.get_attribute('src')
                r = requests.get(download_link)
                img = Image.open(BytesIO(r.content))
                ebird_counter = ebird_counter + 1
                img.save(
                    f'{family}/{order}/{sci_name}/{sci_name}-{ebird_counter}{file_ext}')
                time.sleep(5)
                print(download_link)
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="show_more"]').click()
        except:
            driver.quit()

    print(f'Total url extracted: {ebird_counter}')


def test_search():
    ebird_url = 'https://ebird.org/explore'
    chromeDriver = 'C:\\Users\\jmentore\\Documents\\Selenium Chrome Driver\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chromeDriver)
    driver.get(ebird_url)
    driver.maximize_window()
    element = driver.find_element_by_xpath(
        '//*[@id="Suggest-0"]').send_keys('Otus sunia')

    # select by visible text
    drop_list = select(element)
    drop_list.select_by_visible_text('Otus sunia')
    time.sleep(5000)


def search_byTaxcode(tax_code):
    taxon_code = tax_code
    ebird_url = f'https://ebird.org/species/{taxon_code}'
    chromeDriver = 'C:\\Users\\jmentore\\Documents\\Selenium Chrome Driver\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chromeDriver)
    driver.get(ebird_url)
    view_all = driver.find_element(
        By.XPATH, '/html/body/div/div[7]/div/div/div[2]/div[1]/a')
    time.sleep(5)

    print("WAITING WAITING")
    view_all.click()
    print("View All Clicked")
    time.sleep(5)
    driver.quit()


def trash():
    try:
        wait = WebDriverWait(driver, 10)
        view_all = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'Button Button--small Button--link')))
        view_all.click()
        print("View All button has been clicked")
        return True
    except (TimeoutException, NoSuchElementException) as e:
        print(str(e))
        return False


NEW_download_from_CSV()
# search_bySpecies()

# search_byTaxcode('zimant1')
