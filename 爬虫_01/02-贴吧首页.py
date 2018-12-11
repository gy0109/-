import requests


class TieBa(object):
    def __init__(self):
        self.tieba_name = input('请输入贴吧名字: ')
        self.url = 'http://tieba.baidu.com/f'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    def search_page(self):
        while True:
            search_type = input('请选择要爬取的类型: 单页(n) 多页(m)')
            if search_type.lower() == 'n':
                page = input('请输入要爬取的页数:')
                break
            elif search_type.lower() == 'm':
                page = input('请输入要爬取的总页数:')
                break
            else:
                print('您输入的选项不存在,请重新输入!')
        return int(page)

    def send_request(self, user_params):
        return requests.get(self.url, headers=self.headers, params=user_params).content

    def single_save(self, page, data):
        filename = 'html/' + str(page) + '-tieba.html'
        print('正在下载的是%s文件' % filename)
        with open(filename, 'wb') as f:
            f.write(data)

    # def many_save(self, page, data):
    #     filename = 'html/' + page + '-tieba.html'
    #     with open(filename, 'wb') as f:
    #         f.write(data)

    def run(self):
        page = self.search_page()
        while True:
            params = {
                'kw': self.tieba_name,
                'pn': page
            }
            data = self.send_request(params)
            self.single_save(page, data)
            page += 1


if __name__ == '__main__':
    TieBa().run()
    # TieBa().search_page()
