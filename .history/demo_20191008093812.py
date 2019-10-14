def download_species_byOrder(bird_family, bird_order, bird_species):
    ebird_url = 'https://ebird.org/media/catalog?taxonCode=bludac1&sort=rating_rank_desc&mediaType=p&regionCode='
    chromeDriver = 'C:\\Users\\jmentore\\Documents\\Selenium Chrome Driver\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chromeDriver)
    driver.get(ebird_url)
    ids = driver.find_elements_by_tag_name('img')
    sci_name = bird_species
    family = bird_family
    order = bird_order
    ebird_counter = 0
    file_ext = '.jpg'
    show_more = driver.find_element_by_id('show_more')

    while show_more.is_displayed():
        for ii in ids:
            download_link = ii.get_attribute('src')
            r = requests.get(download_link)
            img = Image.open(BytesIO(r.content))
            ebird_counter = ebird_counter + 1
            img.save(f'{family}/{order}/{sci_name}-{ebird_counter}{file_ext}')
            time.sleep(2)
            print(download_link)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="show_more"]').click()

    print(f'Total url extracted: {ebird_counter}')
    # f.close()  # Close the file
    time.sleep(40000)
    driver.close()
