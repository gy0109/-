import requests


class RenRen(object):
    def __init__(self):
        pass

    def send_request(self):
        return requests.get(self.url, headers=self.headers).content.decode()

    def save_file(self, data):
        with open('', 'wb') as f:
            f.write(data)

    def run(self):
        self.save_file(self.send_request())


if __name__ == '__main__':
    RenRen().run()