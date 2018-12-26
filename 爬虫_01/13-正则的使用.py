import re


def base_use():
    str1 = '''
    qwewerer
    DDDWqqqK
    21243kdf
    '''
    # pattern = re.compile('a(.*)b', re.DOTALL)
    # pattern = re.compile('a(.*)b', re.S)
    # pattern = re.compile('a(.*)b', re.S | re.I)
    pattern = re.compile('a(.*)b', re.S | re.IGNORECASE)

    result = pattern.findall(str1)
    print(result)

    str2 = r'a\nb'
    str3 = r'A\nB'
    print(str3)
    print(str2)


def advanced_use():
    pattern_num = re.compile('^\d+$')
    str_num = '1234dsfd'

    result1 = pattern_num.match(str_num)   # 从头开始
    result2 = pattern_num.search(str_num)   # 任意位置
    result3 = pattern_num.findall(str_num)  # 查找全部--返回list
    print(result1)
    print(result2)
    print(result3)
    str4 = 'bdbbsbdfsbfasdjfioew'
    pattern = re.compile('b')
    iter_result = pattern.finditer(str4)
    for res in iter_result:
        print(res.group())
    print(iter_result)


if __name__ == '__main__':
    base_use()
    advanced_use()

