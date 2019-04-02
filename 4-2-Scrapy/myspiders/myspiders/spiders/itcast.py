# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 数据提取方法， response可直接xpath
        names = response.xpath('//div[@class="tea_con"]//li/div/h3/text()')
        print(names)

        li_list = response.xpath('//div[@class="tea_con"]//li')
        item = {}
        for li in li_list:
            item['name'] = li.xpath('.//h3/text()').extract_first()
            item['level'] = li.xpath('.//h4/text()').extract_first()
            item['text'] = li.xpath('.//p/text()').extract_first()
            print(item)

        yield item

