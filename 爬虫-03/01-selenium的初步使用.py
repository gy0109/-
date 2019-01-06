from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('htttp://www.baidu.com/')   # 请求数据
driver.save_screenshot('长城.png')   # 保存快照
data = driver.page_source             # 打印数据
a_element = driver.find_element_by_id('s_lg_img')  # 查找
# text = a_element.text()  # 取文本数据
# print(text)
# print(a_element.get_attribute(''))   # 取属性

