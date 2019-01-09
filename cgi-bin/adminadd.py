#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests
import datetime
from datetime import timedelta

form = cgi.FieldStorage()
businesscode = form.getvalue('businesscode')
businessname = form.getvalue('businessname')
businessmanager = form.getvalue('businessmanager')
start = form.getvalue('start')
end = form.getvalue('end')
should = form.getvalue('should')
status = "激活"
beyond = "否"
now1 = "0"
businessworker = "none"
workertime = "0"


now = datetime.datetime.now()

monday = now - timedelta(days=now.weekday())
mondaytime = str(monday.year) + '-' + str(monday.month).zfill(2) + '-' + str(monday.day).zfill(2)
last_one_monday = now - timedelta(days=now.weekday() + 7)
last_one_mondaytime = str(last_one_monday.year) + '-' + str(last_one_monday.month).zfill(2) + '-' + str(last_one_monday.day).zfill(2)
last_two_monday = now - timedelta(days=now.weekday() + 14)
last_two_mondaytime = str(last_two_monday.year) + '-' + str(last_two_monday.month).zfill(2) + '-' + str(last_two_monday.day).zfill(2)
last_three_monday = now - timedelta(days=now.weekday() + 21)
last_three_mondaytime = str(last_three_monday.year) + '-' + str(last_three_monday.month).zfill(2) + '-' + str(last_three_monday.day).zfill(2)
last_four_monday = now - timedelta(days=now.weekday() + 28)
last_four_mondaytime = str(last_four_monday.year) + '-' + str(last_four_monday.month).zfill(2) + '-' + str(last_four_monday.day).zfill(2)


db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('INSERT INTO BUSINESS VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");'%(businesscode,businessname,businessmanager,now1,businessworker,workertime,beyond,start,end,should,status))
if mondaytime > start and mondaytime< end:
	cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","none","none","%s","none","0","0","0","0","0","none","0","%s","%s");'%(businesscode,businessname,start,businessmanager,end,mondaytime))
if last_one_mondaytime > start and last_one_mondaytime< end:
	cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","none","none","%s","none","0","0","0","0","0","none","0","%s","%s");'%(businesscode,businessname,start,businessmanager,end,last_one_mondaytime))
if last_two_mondaytime > start and last_two_mondaytime< end:
	cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","none","none","%s","none","0","0","0","0","0","none","0","%s","%s");'%(businesscode,businessname,start,businessmanager,end,last_two_mondaytime))
if last_three_mondaytime > start and last_three_mondaytime< end:
	cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","none","none","%s","none","0","0","0","0","0","none","0","%s","%s");'%(businesscode,businessname,start,businessmanager,end,last_three_mondaytime))
if last_four_mondaytime > start and last_four_mondaytime< end:
	cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","none","none","%s","none","0","0","0","0","0","none","0","%s","%s");'%(businesscode,businessname,start,businessmanager,end,last_four_mondaytime))
db.commit()
db.close()

print("Content-type: text/html\n")

print(should)
