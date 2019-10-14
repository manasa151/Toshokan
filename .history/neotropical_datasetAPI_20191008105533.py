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


def search_bySpecies():
    species = 'Balearica pavonina'
    with open('request_species.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            if species == row[2]:
                makedirs(f'{row[0]}/{row[1]}/{row[2]}', exist_ok=True)
                download_species_byOrder(row[0], row[1], row[2])
                print(row)


def download_species_byOrder(bird_family, bird_order, bird_species):
    driver.maximize_window()
    # ebird_url = driver.find_element(
        By.XPATH, '//*[@id="Suggest-0"]'.send_keys(f'{bird_species}').click())
    time.sleep(2)
    # input search

    ebird_url='https://ebird.org/media/catalog?taxonCode=bludac1&sort=rating_rank_desc&mediaType=p&regionCode='
    chromeDriver='C:\\Users\\jmentore\\Documents\\Selenium Chrome Driver\\chromedriver.exe'
    driver=webdriver.Chrome(executable_path = chromeDriver)
    driver.get(ebird_url)
    ids=driver.find_elements_by_tag_name('img')
    sci_name=bird_species
    family=bird_family
    order=bird_order
    ebird_counter=0
    file_ext='.jpg'
    show_more=driver.find_element_by_id('show_more')

    while show_more.is_displayed():
        for ii in ids:
            download_link=ii.get_attribute('src')
            r=requests.get(download_link)
            img=Image.open(BytesIO(r.content))
            ebird_counter=ebird_counter + 1
            img.save(f'{family}/{order}/{sci_name}-{ebird_counter}{file_ext}')
            time.sleep(2)
            print(download_link)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="show_more"]').click()

    print(f'Total url extracted: {ebird_counter}')
    # f.close()  # Close the file
    time.sleep(400040)
    driver.close()
