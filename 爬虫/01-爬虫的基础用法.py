import requests


class SearchSpilder(object):

    def __init__(self):

        self.url = 'https://www.lagou.com/mycenter/delivery.html?tag=5'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}    # 认为添加headers 防止反爬

    def spider_base(self):
        url_img = 'https://www.lgstatic.com/i/image2/M01/B5/BD/CgotOVwKF5-Ab5gzAAgJyKUVgpM202.PNG'
        # response = requests.get(self.url, headers=headers)   # 获取网页信息
        # response = requests.get(url_img, headers=self.headers)  # 下载图片  图片地址有时候在css中查找

        # print(response.content)
        # print(response.cookies)
        # print(response.status_code)
        # print(response.request_cookies)
        # print(response.headers)
        # print(response.text)     str
        # print(response.url)

        # data = response.content    # bytes

        # with open('01.html', 'wb') as f:
        # with open('01.jpg', 'wb') as f:
        #     f.write(data)

    def send_request(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content

    def save_file(self, filename, data):
        with open(filename, 'wb') as f:
            f.write(data)

    def run(self, filename):
        data = self.send_request()
        self.save_file(filename, data.decode())


if __name__ == '__main__':
    SearchSpilder().run()
