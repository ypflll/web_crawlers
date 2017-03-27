# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import re
import requests
from scrapy.selector import Selector
from hrtencent.items import HrtencentItem
from hrtencent import settings

usr_list1 = []
usr_list2 = []

class hrtencent_xpath(scrapy.Spider):
    name = 'hrtencent-xpath'
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        'http://hr.tencent.com/position.php?keywords=%E7%AE%97%E6%B3%95&lid=0&tid=0',
    ]
    #rules = (Rule(SgmlLinkExtractor(allow=('/post/\d*\.html')),  callback = 'parse_img', follow=True),)
    #rules = (Rule(SgmlLinkExtractor(allow=('/position.php?keywords=%E7%AE%97%E6%B3%95&lid=0&tid=0&start=\d*\0')),  callback = 'parse', follow=True),)
    def parse(self, response):
        item = HrtencentItem()
        for job in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            jd_url = job.xpath('./td[@class="l square"]/a/@href').extract_first()
            jd_url = 'http://hr.tencent.com/' + jd_url
            yield scrapy.Request(jd_url,callback=self.sub_parse)

            job_title = job.xpath('./td[@class="l square"]/a/text()').extract_first()
            number = job.xpath('./td[3]/text()').extract_first()
            location = job.xpath('./td[4]/text()').extract_first()
            date = job.xpath('./td[5]/text()').extract_first()
            usr_list1.append([job_title, number, location, date])

        next_page_url = response.xpath('//a[@id="next"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    def sub_parse(self, response):
        uer_sublist = usr_list[0]
        usr_list.pop(0)

        item = HrtencentItem()
        item['job_title'] = uer_sublist[0]
        item['number'] = uer_sublist[1]
        item['location'] = uer_sublist[2]
        item['date'] = uer_sublist[3]
        item['job_jd'] = response.xpath('//ul[@class="squareli"]/li/text()').extract()
        yield item
