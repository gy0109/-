from selenium import webdriver
dirver = webdriver.PhantomJS()
dirver.get('https://www.lagou.com/mycenter/delivery.html')
dirver.save_screenshot('01baidu.png')   # 截屏 保存快照
data = dirver.page_source  # 打印数据
a_element = dirver.find_element_by_name('')    # 找元素
print(a_element.text)
print(a_element.get_attribute(''))

