import requests
import chardet
import random
import time
from bs4 import BeautifulSoup
from telnetlib import Telnet
import progressbar


user_agent = [
       "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
       "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
       "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
       "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
       "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
       "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
       "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
       "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
       "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
       "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
       "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
       "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
       "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
       "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
       "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"]


def getHtmlWithHeader(url):
	# 尝试获取网页内容，当获取失败的时候重新获取网页代码
	# 当失败次数过多时停止获取 并输出提示信息
    try:
        # 获取响应内容
        response = requests.get(
            url,
            headers={"User-Agent": random.choice(user_agent)}
        )
        # 获取编码
        code = chardet.detect(response.content)["encoding"]
        # 指定编码
        response.encoding = code
        # 输出文本
        # print(response.text)
        return response.text
    except:
        time.sleep(1)
        global _times_count
        _times_count += 1
        if _times_count > 5:
            print("ip获取失败，请稍后重试")
            return
        print("第", _times_count, "次尝试抓取")
        return getHtmlWithHeader(url)


def getIP(num):
    # 准备数据列表
    datalist = []
    # 准备 url
    for num1 in range(num):
        url = 'http://www.xicidaili.com/nn/' + str(num1 + 1)
        # 获取返回数据
        html = getHtmlWithHeader(url)
        soup = BeautifulSoup(html, 'html.parser')
        parent = soup.find(id="ip_list")
        lis = parent.find_all('tr')
        # 删除第一条数据
        lis.pop(0)
        print("爬取ip地址及相关信息")
        for i in lis:
            ip = i.find_all('td')[1].get_text()
            dk = i.find_all('td')[2].get_text()
            nm = i.find_all('td')[4].get_text()
            ty = i.find_all('td')[5].get_text()
            tm = i.find_all('td')[8].get_text()
            datalist.append((ip, dk, nm, ty, tm))
    print("共爬取到", len(datalist), "条数据\n")
    # 将获取到的数据返回
    return datalist


def filtrateIP(datalist):
    datalist1 = []
    # 对生存时间短的数据进行过滤
    print('过滤存活时间短的\n')
    for i in datalist:
        if "分钟" not in i[4]:
            datalist1.append(i)
            # print(i)
    print("共过滤掉", len(datalist) - len(datalist1), "条生存时间短的数据")
    print("还剩", len(datalist1), "条数据\n")

    # 对得到的数据进行测试，看是否可用
    print('测试不可用的ip并将其过滤')
    datalist.clear()
    v = 1
    p = progressbar.ProgressBar()
    for i in p(datalist1):
        # print("正在检测第"+str(v)+"条数据")
        v += 1
        try:
            Telnet(i[0], i[1], timeout=1)
        except:
            pass
        else:
            datalist.append(i)

    print('过滤不可用的ip')
    print("共过滤掉", len(datalist1) - len(datalist), "条不可用数据")
    print("还剩", len(datalist), "条数据")
    # 将过滤后的数据返回
    return datalist


def saveIP(datalist):
    # 对得到的数据进行分类 http/https
    httplist = []
    httpslist = []
    for i in datalist:
        if i[3] == 'HTTP':
            httplist.append('http://' + i[0] + ':' + i[1])
        else:

            httpslist.append('https://' + i[0] + ':' + i[1])
    # 将显示结果显示到屏幕上
    print("HTTP共" + str(len(httplist)) + "条数据")
    print(httplist)
    print("")
    print("HTTPS共" + str(len(httpslist)) + "条数据")
    print(httpslist)
    print("")
    print("写入文件")

    # 打开文件
    f = open('ip地址.txt', 'w', encoding="utf-8")
    # 写入文件
    f.write("HTTP\n")
    f.write(str(httplist) + "\n\n")
    f.write("HTTPS\n")
    f.write(str(httpslist))
    # 关闭文件
    f.close()


def main(num):
    datalist = getIP(num)
    IP_list = filtrateIP(datalist)
    saveIP(IP_list)


if __name__ == '__main__':
    main(1)


