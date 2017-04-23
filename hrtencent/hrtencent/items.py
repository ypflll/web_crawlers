#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Mar 27 2017
@author: pavle
"""

import scrapy

class HrtencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()
    number = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    job_jd = scrapy.Field()
