def add_num():
    # rf = open('html/网站url_02.txt', 'r', encoding='utf-8')
    with open('html/网站url_02.txt', 'r+', encoding='utf-8') as f:
        for i in f.readlines():
           f.write(i.split(' ')[0] + '/0/0.html')


add_num()
