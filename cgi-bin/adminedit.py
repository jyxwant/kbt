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
status = form.getvalue('status')
hasdone = form.getvalue('now')

now = datetime.datetime.now()
now = str(now.year) + '/' + str(now.month).zfill(2) + '/' + str(now.day).zfill(2)

if hasdone > should:
	beyond = "是"
else:
	beyond = "否"
db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('update BUSINESS set BUSINESSNAME="%s",BUSINESSMANAGER="%s", STARTTIME="%s", ENDTIME="%s",SHOULD="%s",STATUS="%s",BEYOND="%s" where  BUSINESSCODE= "%s"'%(businessname,businessmanager,start,end,should,status,beyond,businesscode))
cu.execute('update WORK set PROJECTNAME="%s",STARTTIME="%s",DONE="%s",PROJECTMANAGER="%s",LASTDAY="%s" where PROJECTID="%s"'%(businessname,start,should,businessmanager,end,businesscode))
db.commit()
cu.execute('select PROJECTID,DONE,NOW,MONDAYTIME from WORK')
middle = cu.fetchall()

newdic = []
for key in middle:
	ratio = '' + key[2] + '/' + key[1]
	cu.execute('update WORK set RATIO="%s" where PROJECTID="%s" and MONDAYTIME="%s";'%(ratio,key[0],key[3]))
db.commit()
db.close()



print("Content-type: text/html\n")

print(middle)
