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



db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('INSERT INTO BUSINESS VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");'%(businesscode,businessname,businessmanager,now1,businessworker,workertime,beyond,start,end,should,status))
cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","none","none","%s","none","0","0","0","0","0","none","0","%s","%s");'%(businesscode,businessname,start,businessmanager,end,mondaytime))
db.commit()
db.close()

print("Content-type: text/html\n")

print(should)
