"""
retryIng模块能够实现捕捉函数的异常,反复执行函数的结果,和timeout一起搭配使用,能够解决网络波动带来的请求不成的问题
"""


import retrying
import requests

headers = {}


@retrying.retry(stop_max_attemp_number=3)
def _parse_url(url):
    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    return response


def parse_url(url):
    try:
        response = _parse_url(url)
    except Exception as e:
        print(e)
        response = None
    return response


parse_url('http:www.baidu.com')

