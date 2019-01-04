#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests


form = cgi.FieldStorage()
username = form.getvalue('username')
businesscode = form.getvalue('businesscode')
businessman = form.getvalue('businessman')
mondaytime  = form.getvalue('mondaytime')





db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select * FROM BUSINESS where BUSINESSCODE="%s" and BUSINESSWORKER="%s"'%(businesscode,businessman))
result = cu.fetchall()
lastresult = []

if result == []:
	cu.execute('select * FROM BUSINESS where BUSINESSCODE="%s" '%(businesscode))
	newresult = cu.fetchall()
	for key in newresult:
		k1 = key[3].encode('raw_unicode_escape')
		k2 = key[5].encode('raw_unicode_escape')
		k3 = key[7].encode('raw_unicode_escape')
		k4 = key[8].encode('raw_unicode_escape')
		k5 = key[9].encode('raw_unicode_escape')
		k6 = key[10].encode('raw_unicode_escape')
		lastresult.append({"nonedone":k1,"worktime":"0","starttime":k3,"endtime":k4,"should":k5,"status":k6})
		break

else:
	cu.execute('select * FROM BUSINESS where BUSINESSCODE="%s" '%(businesscode))
	newresult = cu.fetchall()
	for key in newresult:
		k1 = key[3].encode('raw_unicode_escape')
		k2 = key[5].encode('raw_unicode_escape')
		k3 = key[7].encode('raw_unicode_escape')
		k4 = key[8].encode('raw_unicode_escape')
		k5 = key[9].encode('raw_unicode_escape')
		k6 = key[10].encode('raw_unicode_escape')
		lastresult.append({"nonedone":k1,"worktime":k2,"starttime":k3,"endtime":k4,"should":k5,"status":k6})
		break



print("Content-type: text/html\n")

print(lastresult)