import json


def json_base_use():
    str_1 = '{"name":"一出好戏","actor":"黄渤"}'
    dict_1 = json.loads(str_1)

    dict_2 = {'name': '一出好戏', 'actor': '黄渤'}
    str_2 = json.dumps(dict_2)

    #     2. fp文件对象 --- python对象dict list互转
    # fp_two = open('json/01-json.json', 'w')
    # dict_two = {"name": "一出好戏", "actor": "黄渤"}
    # json.dump(dict_two, fp_two)

    fp_1 = open('json/01-json.json', 'r')
    difp_1 = json.load(fp_1)
    print(type(difp_1))


if __name__ == '__main__':
    json_base_use()

