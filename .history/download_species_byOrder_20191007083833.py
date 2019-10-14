
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

cache_location = 'C:\\Users\\jmentore\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache'
count = 0


def get_size(start_path=cache_location):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


// TO DO: FOFO & delete file > 200mb


def clear_cache():

    count = 0
    for path, sub_dirs, files in os.walk(cache_location):
        for f in files:
            try:
                if get_size() > 105135540:
                    file_path = os.path.join(path, f)
                    os.remove(file_path)
                    count = count+1
            except(IOError, SyntaxError)as e:
                print('Cache does not need clearing')
                pass

    print("Total Cache files cleared: ", count)


ebird_url = 'https://ebird.org/media/catalog?taxonCode=bludac1&sort=rating_rank_desc&mediaType=p&regionCode='
chromeDriver = 'C:\\Users\\jmentore\\Documents\\Selenium Chrome Driver\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromeDriver)
driver.get(ebird_url)
ids = driver.find_elements_by_tag_name('img')
sci_name = 'Thraupis-episcopus'
family = 'Passeriformes'
order = 'Thraupidae'
ebird_counter = 0
file_ext = '.jpg'


# name the output file to write to local disk
# outputFilename = f'{sci_name}.csv'
# header of csv file to be written
# headers = "Download Location \n"

# opens file, and writes headers
# f = open(outputFilename, "w")

# style="display: none;"
show_more = driver.find_element_by_id('show_more')

if show_more.is_displayed():
    for ii in ids:
        download_link = ii.get_attribute('src')
        r = requests.get(download_link)
        img = Image.open(BytesIO(r.content))
        ebird_counter = ebird_counter + 1
        img.save(f'{family}/{order}/{sci_name}-{ebird_counter}{file_ext}')
        time.sleep(2)
        print(download_link)
    # f.write(download_link + "\n")
    # clear_cache()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="show_more"]').click()

    else:
        break


print(f'Total url extracted: {ebird_counter}')
# f.close()  # Close the file
time.sleep(40000)
driver.close()
