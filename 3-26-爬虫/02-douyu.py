from selenium import webdriver


def douyu():
    driver = webdriver.PhantomJS()
    driver.get('https://www.douyu.com/directory/all')
    driver.save_screenshot('douyu.png')

    a_elenum = driver.page_source
    id_driver = driver.find_element_by_id('live-list-contentbox')
    print(id_driver.text)


douyu()