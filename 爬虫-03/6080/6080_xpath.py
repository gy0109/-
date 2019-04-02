import time
import requests
import random

from multiprocessing import Process
from multiprocessing import JoinableQueue as Queue
from bs4 import BeautifulSoup as bs
"""
爬虫目标: 爬取网站所有的电影跳转url   网站主url+a href进行拼接  
第二部分： 完成爬取所有num.html的页面  并加载播放url    
第三部分： 分页部分的爬取   与爬取合并 （识别最大页数）  +第二部分  分类   +线进协程池
第四部分： 数据筛选清理 
第五部分： 登陆和注册播放   --- 34.html是vip专区
"""


class WebUrl(object):
    def __init__(self):
        self.base_url = 'http://www.px6080.com/whole/{}.html'       # 11.html是喜剧片
        self.page_url = 'http://www.px6080.com/whole/{}_______0_addtime_{}.html'
        self.USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
]
        self.proxy_list = [
            {"http": '61.135.217.7:80'},
            {"http": '119.39.238.55:9999'},
            # {"http": '119.101.116.136:9999'},
            # {"http": '119.101.115.84:9999'},
            # {"http": '119.101.116.114:9999'},
            {"http": '119.101.113.130:9999'},
            # {"http": '111.155.116.229:8123'},
            # {'http': '119.101.114.239:9999'},
            # {'http': '118.187.58.34:53281'},
            # {'http': '119.101.114.239:9999'},
            # {'http': '118.187.58.34:53281'},
            # {'http': '119.101.115.158:9999'},
            # {'http': '119.101.113.173:9999'},
            # {'http': '119.101.114.143:9999'},
            # {'http': '119.101.116.134:9999'}
        ]
        self.count = 0
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_list_queue = Queue()

    def joint_url(self):
        url_list = []
        for i in range(1, 36):   # 页面到27
            url_list.append(self.base_url.format(i))
        return url_list

    def joint_page__url(self):
        url_list = []
        for i in range(1, 36):   # 页面到27
            for j in range(1, 5):
                self.url_queue.put(self.page_url.format(i, j))
                # url_list.append(self.page_url.format(i, j))
            # with open('html/url_list', 'w', encoding='utf-8')as f:
            #     for url in url_list:
            #         f.write(url + '\r\n')
        return url_list

    def send_request(self):
        response_list = []
        proxy = random.choice(self.proxy_list)  # 随机的代理
        for url in self.joint_url():
            response_list.append(requests.get(url, headers={"User-Agent": random.choice(self.USER_AGENT_LIST)}, proxies=proxy).content.decode())
        # response = requests.get(self.base_url, headers={"User-Agent": random.choice(self.USER_AGENT_LIST)}, proxies=proxy).content.decode()
        print(response_list, '----------------------')
        return response_list

    def save_data(self, data):
        with open('html/网站url_05_分页.txt', 'a', encoding='utf-8') as f:
            f.write(data)

    def parse_data(self, data):
        content_list = []
        title_str_list = []
        href_str_list = []
        href_list = []
        num = 0
        # 解析数据  使用bs4
        soup = bs(data, 'html5lib')
        print('=====', soup, '================')
        # soup_list = soup.select('.movielist ul li a')
        soup_list = soup.select('.col-md-1-5 a')
        for i in soup_list:
            href_str_list.append(i.get('href'))
            title_str_list.append(i.get('title'))  # img有title 取哪个都无所谓http://www.xo55.com
        for index in range(1, len(title_str_list)+1):
            if index % 2 == 0:    # 整除得0
                title_str = title_str_list[index - 1]
                if index <= len(href_str_list) - 1:
                    href_list.append(href_str_list[index - 1].split('/', 2)[2])
                    content_str = title_str + '-----' + 'http://www.px6080.com' + href_str_list[index - 2] + '      播放页面：' + 'http://www.px6080.com/play/' + href_list[num].split('.')[0] + '/0/0.html' + '\r\n'
                    # print(content_str)
                    content_list.append(content_str)
                    num += 1
                index += 1
        print(content_list)
        return content_list

    def start_spider(self):
        content_list = []
        for data in self.send_request():
            content_list.append(self.parse_data(data))
        # content_list = self.parse_data(self.send_request())
        for i in content_list:
            for j in i:
                self.save_data(j)

    def run(self):
        start_time = time.time()
        self.start_spider()
        end_time = time.time()
        print('共耗时%s' % (end_time - start_time))


if __name__ == '__main__':
    WebUrl().run()
