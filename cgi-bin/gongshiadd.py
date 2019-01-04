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
mondaytime = form.getvalue('mondaytime')
username  = form.getvalue('username')

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select PROJECTNAME,STARTTIME,DONE,RATIO,PROJECTMANAGER,NOW,LASTDAY from WORK where PROJECTID="%s" and JUDGE="none"'%(businesscode))
result = cu.fetchall()

lastresult = []
for key in result:
	k1 = key[0].encode('raw_unicode_escape')
	k2 = key[1].encode('raw_unicode_escape')
	k3 = key[2].encode('raw_unicode_escape')
	k4 = key[3].encode('raw_unicode_escape')
	k5 = key[4].encode('raw_unicode_escape')
	k6 = key[5].encode('raw_unicode_escape')
	k7 = key[6].encode('raw_unicode_escape')
	lastresult.append({"businessname":k1,"starttime":k2,"done":k3,"ratio":k4,"businessmanager":k5,"now":k6,"endtime":k7})
#cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","%s","%s","%s","%s","0","0","0","0","0","未提交","%s","%s","%s");'%(businesscode,result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],username,result[0][5],result[0][6],mondaytime))
#db.commit()
#db.close()

print("Content-type: text/html\n")

print(lastresult)
