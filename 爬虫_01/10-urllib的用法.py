import urllib.request as urllib


def base_use_urllib():
    url = 'http://www.baidu.com'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    # 创建请求对象
    request = urllib.Request(url, headers=headers)
    # 系统自带的方法  获取响应
    response = urllib.urlopen(request)
    data = response.read().decode()   # bytes类型
    print(response)
    print(request)
    print(data)


if __name__ == '__main__':
    base_use_urllib()
