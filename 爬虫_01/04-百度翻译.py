import requests
# 需求: 利用百度翻译完成网页翻译


class BaiduFanYi(object):
    def __init__(self):
        self.url = 'https://fanyi.baidu.com/#/zh/en/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    def send_request(self):
        return requests.get(self.url, headers=self.headers).content.decode()

    def save_file(self, data):
        with open('', 'wb') as f:
            f.write(data)

    def run(self):
        self.save_file(self.send_request())


if __name__ == '__main__':
    BaiduFanYi().run()
