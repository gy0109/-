import requests


class TieBa(object):
    def __init__(self):
        self.tieba_name = input('请输入贴吧名字: ')
        self.url = 'http://tieba.baidu.com/f'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    def send_request(self, user_params):
        return requests.get(self.url, headers=self.headers, params=user_params).content

    def save_file(self, filename, data):
        with open(filename, 'wb') as f:
            f.write(data)

    def run(self, filename):
        params = {
            'kw': self.tieba_name,
            'pn': 0
        }
        data = self.send_request(params)
        self.save_file(filename, data)


if __name__ == '__main__':
    TieBa().run('html/02-tieba.html')
