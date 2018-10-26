# -*- coding: utf-8 -*-
import scrapy
from meiju110.items import Meiju110Item

from scrapy.http import Request

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    }

    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):

        items = []
        subSelector = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for sub in subSelector:
            item = Meiju110Item()
            item['storyName'] = sub.xpath('./h5/a/text()').extract()
            item['storyState'] = sub.xpath('./span[1]/font/text()').extract()
            if item['storyState']:
                pass
            else:
                item['storyState'] = sub.xpath('./span[1]/text()').extract()
            item['storyCatagory'] = sub.xpath('./span[2]/text()').extract()
            if item['storyCatagory']:
                pass
            else:
                item['storyCatagory'] = [u'未知']

            item['tvStation'] = sub.xpath('./span[3]/text()').extract()
            if item['tvStation']:
                pass
            else:
                item['tvStation'] = [u'未知']

            item['updateTime'] = sub.xpath('./div[2]/font/text()').extract()
            if item['updateTime']:
                pass
            else:
                item['updateTime'] = sub.xpath('./div[2]/text()').extract()
            items.append(item)
        return items
