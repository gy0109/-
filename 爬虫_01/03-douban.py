import requests


class Douban(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=&start=0&limit-20'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    def send_request(self):
        return requests.get(self.url, headers=self.headers).content.decode()

    def save_file(self, data):
        with open('html/04-doubian.json', 'w') as f:
            f.write(data)

    def run(self):
        data = self.send_request()
        self.save_file(data)


if __name__ == '__main__':
    Douban().run()

