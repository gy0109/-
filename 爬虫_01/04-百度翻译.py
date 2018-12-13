import json

import requests
# 需求: 利用百度翻译完成网页翻译


class BaiduFanYi(object):
    def __init__(self):
        self.translate_content = input('请输入要翻译的内容:')
        """"
        查找移动端的整个过程: 检查左上角的手机移动端模式  选择手机类型 刷新页面  检查xhr的basetran 下面的headers中找到User-Agent 和url  打印data 进行json转译 查看字典下的 字段  进行拼接
        """
        self.url = 'https://fanyi.baidu.com/basetrans'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36"}


    def send_request(self, translate_data):
        # post请求  和参数的使用
        return requests.post(self.url, headers=self.headers, data=translate_data).content.decode()

    def parse_data(self, data):
        dict_data = json.loads(data)
        result = dict_data['trans'][0]['result'][0][1]
        print('翻译的结果是%s' % result)
        # print(data)

    def run(self):
        form_data = {
            'query': self.translate_content,
            'from': 'zh',
            'to': 'en'
        }
        self.parse_data(self.send_request(form_data))


if __name__ == '__main__':
    BaiduFanYi().run()
