import gevent.monkey
from gevent.pool import Pool
from queue import Queue
import requests
from bs4 import BeautifulSoup as bs
import time
import random

gevent.monkey.patch_all()


class QiuShiSplier(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/text/page/{}'   # 所有的页数
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        self.count = 0
        self.add_count = 1500
        self.url_queue = Queue()
        self.pool = Pool()
        self.response_count = 0     # 响应和请求数    并发时  当响应数大于请求数时 关闭线程池
        self.request_count = 0
        self.is_runnig = True    # 是否继续的开关

    # 组合所有的url列表
    def get_url_list(self):
        for i in range(1, 6):    # 从url池中获取url
            self.url_queue.put(self.base_url.format(i))
            self.request_count += 1

    # 发送请求   从url池中获取url进行访问
    def send_request(self, url):
        while True:
            # time.sleep(2)   # 此处取到一个url, 陷入死循环
            # print(url)      # 此处传入url   所以要在传进去的地方进行遍历url队列     取出不同的url
            proxy_list = [
                # {"http": '111.155.116.229:8123'},
                {'http': '119.101.114.239:9999'},
                {"http": '61.135.217.7:80'},
                {'http': '118.187.58.34:53281'}
            ]     # 代理IP
            proxy = random.choice(proxy_list)    # 随机的代理
            # print(url)
            response = requests.get(url, headers=self.headers, proxies=proxy)   # 发出请求   响应数+1
            self.response_count += 1
            self.url_queue.task_done()      # 任务启动   单纯使用get不会使队列数-1  需要和task_done进行配合使用
            return response.content.decode()

    # 解析数据
    def get_content_list(self, data):
        print(data)
        content_list = []
        if self.count <= self.add_count:
            while True:
                soup = bs(data, 'html5lib')
                soup_list = soup.select('.content span')
                for div in soup_list:
                    content = {}    # 每次都创建一个新的dict 不然会覆盖
                    content_div = div.get_text()
                    content['content'] = content_div
                    content_list.append(content)
                    self.count += 1
                if self.count >= self.add_count:     # 中断死循环的条件  一次取500字节
                    break
            self.add_count += 1000
        return content_list

    # 保存数据
    def save_file(self, data):
        with open('html/04-thread_pool.txt', 'a', encoding='utf-8') as f:
            f.write(data)

    def _excute_request_response_item(self):
        url = self.url_queue.get()
        print(url)
        data = self.send_request(url)
        for i in self.get_content_list(data):   # 循环追加
            self.save_file(i['content'])
        self.response_count += 1

    # def _callback(self):
    #     if self.is_runnig:
    #         self.pool.apply_async(self._excute_request_response_item())    # 回调函数

    def start_work(self):
        # 获取url队列
        self.get_url_list()
        # 请求解析保存数据 开启异步任务 设置并发数
        for i in range(3):
            # print('这是第%s个url' % i)
            self.pool.apply_async(self._excute_request_response_item())   # 协程池异步的方法
        while True:
            time.sleep(0.001)
            if self.response_count >= self.request_count:
                self.is_runnig = False
                break

    # 调度
    def run(self):
        start_time = time.time()
        self.start_work()
        end_time = time.time()
        print('一共耗时:', end_time-start_time)


if __name__ == '__main__':
    QiuShiSplier().run()
