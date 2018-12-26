from queue import Queue
from multiprocessing import Process
from multiprocessing import JoinableQueue as Queue
import requests
from lxml import etree
import time
import random


class QiuShiSplier(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/text/page/{}'   # 所有的页数
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        self.count = 0
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_list_queue = Queue()

    # 组合所有的url列表
    def get_url_list(self):
        for i in range(1, 18):
            self.url_queue.put(self.base_url.format(i))

    # 发送请求   从url池中获取url进行访问
    def send_request(self):
        while True:
            url = self.url_queue.get().content.decode()
            proxy_list = [
                {"http": '111.155.116.229:8123'},
                {"http": '61.135.217.7:80'},
            ]
            proxy = random.choice(proxy_list)
            response = requests.get(url, headers=self.headers, proxies=proxy)

            if response.status_code == 200:
                self.html_queue.put(response)
            else:
                self.url_queue.put(url)

            self.url_queue.task_done()

    # 解析数据
    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            html_data = etree.HTML(html_str)
            div_list = html_data.xpath('//div[@id="content-left"]/div')
            content_list = []
            content = {}
            for div in div_list:
                content['content'] = div.xpath(".//div[@class='content']/span/text()")[0]
                print(content)
                content_list.append(content)
            self.content_list_queue.put(content_list)
            self.html_queue.task_done()

    # 保存数据
    def save_file(self):
        while True:
            content_list = self.content_list_queue.get()
            self.content_list_queue.task_done()

    def start_work(self):
        th_list = []
        # 1,组合url_list
        th_url = Process(target=self.get_url_list)
        th_list.append(th_url)
        # 2,发送请求 并发数
        for i in range(2):
            th_request = Process(target=self.send_request)
            th_list.append(th_request)
        # 3,解析
        th_alysis = Process(target=self.get_content_list)
        th_list.append(th_alysis)

        # 4,保存
        th_save = Process(target=self.save_file)
        th_list.append(th_save)

        for th in th_list:
            th.daemon(True)   # 线程守护 py3主线程挂了 子线程不挂
            th.start()

        for qu in [self.url_queue, self.html_queue, self.content_list_queue]:
            qu.join()

    # 调度
    def run(self):
        start_time = time.time()
        self.start_work()
        end_time = time.time()
        print('一共耗时:', end_time-start_time)


if __name__ == '__main__':
    QiuShiSplier().run()
