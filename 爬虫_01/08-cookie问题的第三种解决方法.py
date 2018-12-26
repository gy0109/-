import requests


def renren_login():
    base_url = 'http://www.renren.com/918315005/profile'
    login_url = 'https://www.renren.com/PLogin.do'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    # cookie的第三种实现方案 session.post(_)请求登录页面
    form_data = {
        'email': 'gy980109',
        "password": "gaoyan0109"}
    session = requests.session()
    session.post(login_url, headers=headers, data=form_data)

    data = session.get(base_url, headers=headers, ).content.decode()
    with open('html/07-renrenlogin.html', 'w', encoding='utf8') as f:
        f.write(data)


if __name__ == '__main__':
    renren_login()


