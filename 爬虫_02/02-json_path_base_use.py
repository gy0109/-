import jsonpath
import requests


def jsonpath_base_use():
    url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    response = requests.get(url, headers=headers)
    # data_content = response.content.decode()
    data_json = response.json()    # 网站结尾必须是.json的 才能使用json()方法  返回的结果是dict 和 list

    print(jsonpath.jsonpath(data_json, '$..name'))


if __name__ == '__main__':
    jsonpath_base_use()
