# -*- coding: utf-8 -*-
#File name :spyders/mokospider.py
#Author:Jhonny Zhang
#mail:veinyy@163.com
#create Time : 2014-11-29
#############################################################################

from scrapy.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from moko.items import MokoItem
import re
from scrapy.http import Request
from scrapy.selector import Selector


class MokoSpider(CrawlSpider):
    name = "moko"
    allowed_domains = ["moko.cc"]
    start_urls=["http://www.moko.cc/post/aaronsky/list.html"]
    rules = (Rule(SgmlLinkExtractor(allow=('/post/\d*\.html')),  callback = 'parse_img', follow=True),)
    
    def parse_img(self, response):
        urlItem = MokoItem()
        sel = Selector(response)
        for divs in sel.xpath('//div[@class="pic dBd"]'):
            img_url=divs.xpath('.//img/@src2').extract()[0]
            urlItem['url'] = img_url
            yield urlItem
