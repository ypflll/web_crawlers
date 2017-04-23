#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Mar 27 2017
@author: pavle
"""

import MySQLdb as db

#the default encoding is ascii, change to unicode when have chinese word
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


sql_create = """create table algrithm_engineer (date date, job_title char(100), 
	number tinyint, location char(10), job_description varchar(2000))"""

class HrtencentPipeline(object):
	def __init__(self):
		my_db = db.connect('127.0.0.1', 'user', 'passwd', 'hr_tencent')
		cursor = my_db.cursor()
		cursor.execute("drop table if exists algrithm_engineer")
		cursor.execute(sql_create)

	def process_item(self, item, spider):
		my_db = db.connect('127.0.0.1', 'user', 'passwd', 'hr_tencent')
		cursor = my_db.cursor()

		#set the varibales to utf-8
		cursor.execute("SET NAMES utf8")
		
		sql_insert = """insert into algrithm_engineer (date, job_title, number, location, job_description) \
			value ('%s', '%s', '%d', '%s', '%s')""" \
			% (str(item['date']), str(item['job_title']) ,int(item['number']),\
			str(item['location']), str(item['job_jd']))

		try:
			cursor.execute(sql_insert)
			my_db.commit()
		except:
			print 'Failed to add one record!'
			my_db.rollback()

		return item