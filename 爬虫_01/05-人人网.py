import requests


class RenRenLogin(object):
    def __init__(self):
        self.base_url = 'http://zhibo.renren.com/liveroom/2386700'
        # 添加cookie的第一种方法: headers添加cookie
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                        'Cookie': '_r01_=1; anonymid=jl0rk3uv-9k9uyp; depovince=BJ; ick_login=4cf3e978-a02f-43c3-bb6a-4012eb33681b; t=1cd6fa285107b4b38ba02be018edccac4; societyguester=1cd6fa285107b4b38ba02be018edccac4; id=969100784; xnsid=5a7f5b07; jebecookies=fd4874a2-451b-4355-bc4f-d69c829b5a77|||||; ver=7.0; loginfrom=null; jebe_key=d732c6b7-1b16-4132-a66f-f19715021abe%7Ceb1a82dfefad5d18ecd9edca3ff8e9a0%7C1544669935639%7C1%7C1544669936365; JSESSIONID=abc1uJ3oERY0sgxVPGLEw; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1544670062; _ga=GA1.2.2082837777.1544670062; _gid=GA1.2.556184408.1544670062; _ga=GA1.3.2082837777.1544670062; _gid=GA1.3.556184408.1544670062; _gat=1; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1544671052; _gat_UA-88837644-1=1'}

    def send_request(self):
        return requests.get(self.base_url, headers=self.headers).content.decode()

    def save_file(self, data):
        with open('html/05-renrenlogin.html', 'w', encoding='utf8') as f:
            f.write(data)

    def run(self):
        self.save_file(self.send_request())


if __name__ == '__main__':
    RenRenLogin().run()


