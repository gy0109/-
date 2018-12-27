from multiprocessing.dummy import Pool
from queue import Queue
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
        self.pool = Pool()
        self.response_count = 0     # 响应和请求数    并发时  当响应数大于请求数时 关闭线程池
        self.request_count = 0
        self.is_runnig = True    # 是否继续的开关

    # 组合所有的url列表
    def get_url_list(self):
        for i in range(1, 18):    # 从url池中获取url
            self.url_queue.put(self.base_url.format(i))

    # 发送请求   从url池中获取url进行访问
    def send_request(self, url):
        while True:
            time.sleep(2)
            print(url)
            proxy_list = [
                {"http": '111.155.116.229:8123'},
                {"http": '61.135.217.7:80'},
            ]     # 代理IP
            proxy = random.choice(proxy_list)    # 随机的代理
            response = requests.get(url, headers=self.headers, proxies=proxy)   # 发出请求   响应数+1
            self.response_count += 1
            self.url_queue.task_done()      # 任务启动   单纯使用get不会使队列数-1  需要和task_done进行配合使用
            return response.content.decode()

    # 解析数据
    def get_content_list(self, data):
        while True:
            html_data = etree.HTML(data)    # lxml 解析HTML数据的
            div_list = html_data.xpath('//div[@id="content-left"]/div')   # lxml
            content_list = []
            content = {}
            for div in div_list:
                content['content'] = div.xpath(".//div[@class='content']/span/text()")[0]
                print(content)
                content_list.append(content)
                self.count += 1
                print('总个数为:', self.count)

    # 保存数据
    def save_file(self, data):
        with open('html/04-thread_pool.txt', 'w', encoding='utf-8') as f:
            f.write(data)

    def _excute_request_response_item(self):
        url = self.url_queue.get()
        data = self.send_request(url)
        return self.get_content_list(data)

    def callback(self):
        if self.is_runnig:
            self.pool.apply_async(self._excute_request_response_item(), callback=self.callback)    # 回调函数

    def start_work(self):
        # 获取url队列
        self.get_url_list()
        # 请求解析保存数据 开启异步任务 设置并发数
        for i in range(3):
            self.pool.apply_async(self._excute_request_response_item(), callback=self.callback)

        while True:
            time.sleep(0.001)
            if self.response_count >= self.request_count:
                self.is_runnig = False
                break

        self.pool.close()   # 线程池关闭
        self.pool.join()   # 线程阻塞

    # 调度
    def run(self):
        start_time = time.time()
        self.start_work()
        end_time = time.time()
        print('一共耗时:', end_time-start_time)


if __name__ == '__main__':
    QiuShiSplier().run()
