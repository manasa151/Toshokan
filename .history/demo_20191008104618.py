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

driver.maximize_window()
ebird_url = driver.find_element(By.XPATH, '//*[@id="Suggest-0"]'.send_keys(f'{bird_species}')
chromeDriver='C:\Users\jmentore\Documents\Selenium Chrome Driver\chromedriver.exe'
driver=webdriver.Chrome(executable_path=chromeDriver)
driver.get(ebird_url)
