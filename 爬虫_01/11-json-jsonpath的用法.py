import json
import jsonpath
import requests


def json_base_use():
    str1 = '{"name": "\u4e00\u51fa\u597d\u620f", "actor": "\u9ec4\u6e24"}'
    print(json.loads(str1))
    dict2 = {'name': 'xiaoming', 'age': 18}
    print(json.dumps(dict2))

    with open('html/01-json.json', 'w', encoding='utf8') as fp1:
        json.dump(dict2, fp1)

    with open('html/01-json.json', 'r') as fp2:
        print(type(json.load(fp2)))


def jsonpath_base_use():
    # .json结尾的网页如何获取????
    url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    response = requests.get(url, headers=headers)
    data = response.json()
    city_name = jsonpath.jsonpath(data, '$..id')
    print(city_name)


def store_json():
    with open('html/02-store.json', 'r', encoding='utf8') as f:
        print(jsonpath.jsonpath(f.read(), '$.store.*'))


def douban_jsonpath():
    url = 'https://m.douban.com/tv/'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    print(json_data)
    # meiguo = jsonpath.jsonpath(json_data)
    # yingguo = jsonpath.jsonpath(json_data)


if __name__ == '__main__':
    # json_base_use()
    # jsonpath_base_use()
    store_json()
    # douban_jsonpath()
