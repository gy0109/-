import requests


def use_cookiejar():
    url = 'https://www.baidu.com/'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    response = requests.get(url, headers=headers)
    print(type(response.cookies))

    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    print(cookies)


if __name__ == '__main__':
    use_cookiejar()