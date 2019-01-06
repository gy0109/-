import time
import requests
import random

from bs4 import BeautifulSoup as bs
"""
爬虫目标: 爬取网站所有的电影跳转url   网站主url+a href进行拼接
"""


class WebUrl(object):
    def __init__(self):
        self.base_url = 'http://www.px6080.com/whole/33_______0_addtime_3.html'       # 11.html是喜剧片
        self.USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
]
        self.proxy_list = [
            {"http": '61.135.217.7:80'},
            {"http": '119.39.238.55:9999'},
            # {"http": '119.101.116.136:9999'},
            {"http": '119.101.115.84:9999'},
            # {"http": '119.101.116.114:9999'},
            # {"http": '119.101.113.130:9999'},
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

    # def joint_url(self):
    #     url_list = []
    #     for i in range(1, 28):   # 页面到27
    #         url_list.append(self.base_url.format(i))
    #         print(url_list)
    #     return url_list

    def send_request(self):
        # response_dict = {}
        proxy = random.choice(self.proxy_list)  # 随机的代理
        # for url in self.joint_url():
            # response_dict['response'] = requests.get(url, headers={"User-Agent": random.choice(self.USER_AGENT_LIST)}, proxies=proxy).content.decode()
        response = requests.get(self.base_url, headers={"User-Agent": random.choice(self.USER_AGENT_LIST)}, proxies=proxy).content.decode()
        return response

    def save_data(self, data):
        with open('html/网站url_01.txt', 'a', encoding='utf-8') as f:
            f.write(data)

    def parse_data(self, data):
        content_list = []
        title_str_list = []
        href_str_list = []
        # 解析数据  使用bs4
        soup = bs(data, 'html5lib')
        # soup_list = soup.select('.movielist ul li a')
        soup_list = soup.select('.col-md-1-5 a')
        for i in soup_list:
            href_str_list.append(i.get('href'))
            title_str_list.append(i.get('title'))  # img有title 取哪个都无所谓http://www.xo55.com
        for index in range(1, len(title_str_list)+1):
            if index % 2 == 0:    # 整除得0
                title_str = title_str_list[index - 1]
                if index <= len(href_str_list) - 1:
                    content_str = title_str + '-----' + 'http://www.px6080.com' + href_str_list[index - 1] + '\r\n'
                    content_list.append(content_str)
                index += 1
            # else:
            #     href_index = index + 1
            #     title_str = title_str_list[href_index - 1]
            #     if index <= len(href_str_list) - 1:
            #         content_str = title_str + '-----' + 'http://www.px6080.com' + href_str_list[index] + '\r\n'
            #         content_list.append(content_str)
        # for i in soup_list:
        #     href_str = i.get('href')
        #     title_str = i.get('title')  # img有title 取哪个都无所谓http://www.xo55.com
        #     content_str = title_str + '-----' + 'http://www.px6080.com/whole' + href_str + '\r\n'
        #     content_list.append(content_str)
        print(content_list)
        return content_list

    def start_spider(self):
        # content_list = []
        # for data in self.send_request():
        #     content_list.append(self.parse_data(data[1]))
        content_list = self.parse_data(self.send_request())
        for i in content_list:
            self.save_data(i)

    def run(self):
        start_time = time.time()
        self.start_spider()
        end_time = time.time()
        print('共耗时%s' % (end_time - start_time))


if __name__ == '__main__':
    WebUrl().run()
