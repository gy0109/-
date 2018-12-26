import requests
from lxml import etree
import time


class QiuShiSplier(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/text/page/{}'   # 所有的页数
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        self.count = 0

    # 组合所有的url列表
    def get_url_list(self):
        return [self.base_url.format(i)for i in range(1, 18)]

    # 发送请求
    def send_request(self, url):
        return requests.get(url, headers=self.headers).content.decode()

    # 解析数据
    def analy_data(self, data):
        html_data = etree.HTML(data)
        div_list = html_data.xpath('//div[@id="content-left"]/div')
        url_list = []
        for div in div_list:
            nick_name = div.xpath('.//span/text()')[0]
            print(nick_name)
            self.count += 1
            url_list.append(nick_name)


    # 保存数据
    def save_file(self, data):
        # with open('html/01-qiushibaile.html', 'w', encoding='utf8')as f:
        #     f.write(data)
        with open('html/01-qiushibaile.txt', 'w', encoding='utf8')as f:
            f.write(data)
        print(data)

    # 开始爬取数据
    def start_spliter_data(self):
        url_list = self.get_url_list()
        for url in url_list:
            data = self.send_request(url)
            result = self.analy_data(data)
            self.save_file(result)
        print(self.count)

    # 调度
    def run(self):
        start_time = time.time()
        self.start_spliter_data()
        end_time = time.time()
        print('一共耗时:', end_time-start_time)


if __name__ == '__main__':
    QiuShiSplier().run()
