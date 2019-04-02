import requests
import threading
from lxml import etree
from queue import Queue


class Qiubai(object):
    def __init__(self):
        self.temp_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X \
                10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_list_queue = Queue()

    def get_url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.temp_url.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@id='content-left']/div")
            content_list = []
            for div in div_list:
                content = {}
                content["content"] = div.xpath(".//div[@class='content']/span/text()")
                content_list.append(content)
            self.content_list_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_list_queue.get()
            pass
            self.content_list_queue.task_done()

    def run(self):
        thread_list = []
        # 1.url_list
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # 2.遍历，发送请求，
        for i in range(3):  # 三个线程发送请求
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        # 3.提取数据
        t_content = threading.Thread(target=self.get_content_list)
        thread_list.append(t_content)
        # 4.保存
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)

        for t in thread_list:
            t.setDaemon(True)  # 把子线程设置为守护线程，当前这个线程不重要，主线程结束，子线程技术
            t.start()

        for q in [self.url_queue, self.html_queue, self.content_list_queue]:
            q.join()  # 让主线程阻塞，等待队列的计数为0，

        print("主线程结束")


if __name__ == '__main__':
    qiubai = Qiubai()
    qiubai.run()