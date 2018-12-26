import requests


def renren_login_profile():
    #     1. 目标的url 好友页面
    profile_url = 'http://www.renren.com/489862027/profile'

    #  登录的页面 都是靠 cookie认证 权限的, 只要能拿到cookie 发送请求, 就可以获取目标数据
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }
    # cookies = {
    #     ' _r01_': '1',
    #     'anonymid': 'jl0rk3uv-9k9uyp',
    #     'depovince': 'BJ',
    #     'ick_login': '4cf3e978-a02f-43c3-bb6a-4012eb33681b',
    #     't': '1cd6fa285107b4b38ba02be018edccac4',
    #     'societyguester': '1cd6fa285107b4b38ba02be018edccac4',
    #     'id': '969100784',
    #     'xnsid': '5a7f5b07',
    #     'jebecookies': 'fd4874a2-451b-4355-bc4f-d69c829b5a77|||||',
    #     'ver': '7.0',
    #     'loginfrom': 'null',
    #     'jebe_key': 'd732c6b7-1b16-4132-a66f-f19715021abe%7Ceb1a82dfefad5d18ecd9edca3ff8e9a0%7C1544669935639%7C1%7C1544669936365',
    #     'JSESSIONID': 'abc1uJ3oERY0sgxVPGLEw',
    #     'Hm_lvt_966bff0a868cd407a416b4e3993b9dc8': '1544670062',
    #     '_ga': 'GA1.2.2082837777.1544670062',
    #     '_gid': 'GA1.2.556184408.1544670062',
    #     '_ga': 'GA1.3.2082837777.1544670062',
    #     '_gid': 'GA1.3.556184408.1544670062',
    #     '_gat': '1',
    #     'Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8': '1544671052',
    #     '_gat_UA-88837644-1': '1',
    # }
    #
    # cookies_str = "_r01_=1; anonymid=jl0rk3uv-9k9uyp; depovince=BJ; ick_login=4cf3e978-a02f-43c3-bb6a-4012eb33681b; t=1cd6fa285107b4b38ba02be018edccac4; societyguester=1cd6fa285107b4b38ba02be018edccac4; id=969100784; xnsid=5a7f5b07; jebecookies=fd4874a2-451b-4355-bc4f-d69c829b5a77|||||; ver=7.0; loginfrom=null; jebe_key=d732c6b7-1b16-4132-a66f-f19715021abe%7Ceb1a82dfefad5d18ecd9edca3ff8e9a0%7C1544669935639%7C1%7C1544669936365; JSESSIONID=abc1uJ3oERY0sgxVPGLEw; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1544670062; _ga=GA1.2.2082837777.1544670062; _gid=GA1.2.556184408.1544670062; _ga=GA1.3.2082837777.1544670062; _gid=GA1.3.556184408.1544670062; _gat=1; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1544671052; _gat_UA-88837644-1=1"
    #
    # list_cookies = cookies_str.replace(';', ',').split(', ')
    # cookie_dict = {i.split('=')[0]: i.split('=')[1] for i in list_cookies}

    session = requests.session()  # 自动保存上一次获取的cookie的值
    login_url = 'http://www.renren.com/PLogin.do'
    form_data = {
        'email': '13146128763',
        'password': 'zhoudawei123'
    }
    session.post(profile_url, headers=headers, data=form_data)   # 成功保存的才是有效的cookie

    # 假如成功   解析session的cookie  发送目标请求
    data = session .get(profile_url, headers=headers).content.decode()

    with open('html/04-renren.html', 'w') as f:
        f.write(data)


renren_login_profile()
