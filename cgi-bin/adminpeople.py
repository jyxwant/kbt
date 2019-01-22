#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests
import datetime
from datetime import timedelta
import sys
if sys.getdefaultencoding() != 'utf-8':
	reload(sys)
	sys.setdefaultencoding('utf-8')
form = cgi.FieldStorage() 





#获取时间
now = datetime.datetime.now()

monday = now - timedelta(days=now.weekday())
mondaytime = str(monday.year) + '-' + str(monday.month).zfill(2) + '-' + str(monday.day).zfill(2)


last_one_monday = now - timedelta(days=(now.weekday() + 7))
last_one_mondaytime = str(last_one_monday.year) + '-' + str(last_one_monday.month).zfill(2) + '-' + str(last_one_monday.day).zfill(2)
last_two_monday = now - timedelta(days=(now.weekday() + 14))
last_two_mondaytime = str(last_two_monday.year) + '-' + str(last_two_monday.month).zfill(2) + '-' + str(last_two_monday.day).zfill(2)

last_three_monday = now - timedelta(days=(now.weekday() + 21))
last_three_mondaytime = str(last_three_monday.year) + '-' + str(last_three_monday.month).zfill(2) + '-' + str(last_three_monday.day).zfill(2)

last_four_monday = now - timedelta(days=(now.weekday() + 28))
last_four_mondaytime = str(last_four_monday.year) + '-' + str(last_four_monday.month).zfill(2) + '-' + str(last_four_monday.day).zfill(2)




db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select NAME from WORKER')
username = cu.fetchall()
newname = []

for key in username:
	name = key[0]
	thename = name.encode('raw_unicode_escape')
	cu.execute('select * from WORK where PROJECTWORKER="%s" and (JUDGE="审批通过" or JUDGE="未审批") and MONDAYTIME="%s"'%(name,last_one_mondaytime))
	result = cu.fetchall()
	if result == []:
		newname.append({"name":thename,"mondaytime":last_one_mondaytime})

	cu.execute('select * from WORK where PROJECTWORKER="%s" and (JUDGE="审批通过" or JUDGE="未审批") and MONDAYTIME="%s"'%(name,last_two_mondaytime))

	result = cu.fetchall()
	if result == []:
		newname.append({"name":thename,"mondaytime":last_two_mondaytime})
"""
	cu.execute('select * from WORK where PROJECTWORKER="%s" and (JUDGE="审批通过" or JUDGE="未审批") and MONDAYTIME="%s"'%(name,last_three_monday))
	result = cu.fetchall()
	if result == []:
		newname.append({"name":thename,"mondaytime":last_three_mondaytime})
	cu.execute('select * from WORK where PROJECTWORKER="%s" and (JUDGE="审批通过" or JUDGE="未审批") and MONDAYTIME="%s"'%(name,last_four_monday))
	result = cu.fetchall()
	if result == []:
		newname.append({"name":thename,"mondaytime":last_four_mondaytime})
"""

print("Content-type: text/html\n")

print(newname)


