from bs4 import BeautifulSoup
import re


def base_use_bs4():
    html ="""
        <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())     # 格式化输出为html格式页面
    # print(soup.find_all('b'))  # 查找所有
    # for tag in soup.find_all(re.compile('^b')):
    #     print(tag.name)     # 通过正则表达式的match()来匹配
    # print(soup.find_all(['a', 'b']))
    # print(soup.find_all(id='link2'))
    # print(soup.find_all(text='Elsie'))
    # print(soup.find_all(text=re.compile('Dprmouse')))
    # print(soup.select('a'))      # 标签选择器
    # print(soup.select('.sister'))   # 类选择器
    # print(soup.select('#link1'))   # id选择器
    # print(soup.select('p #link1'))   # 层级选择器
    # print(soup.select("a[class='sister']"))   # 属性选择器
    # print(soup.select('a[href="http://example.com/elsie"]'))    # 属性选择器

    print(soup.select('title'))[0].get_text()   # 获取文本内容

    for title in soup.select('title'):
        print(title.get_text())

    print(soup.select('a')[0].get('href'))    # 获取属性  get()方法


base_use_bs4()
