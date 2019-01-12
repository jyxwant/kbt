#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests


form = cgi.FieldStorage()
start = form.getvalue('start')
end = form.getvalue('end')
username = form.getvalue('username')
mondaytime  = form.getvalue('mondaytime')

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select * from WORK where PROJECTWORKER = "%s" and MONDAYTIME = "%s" and JUDGE != "审批拒绝"'%(username,mondaytime))

result = cu.fetchall()


#转换为json
lastresult = []
for key in result:
	k1 = key[0].encode('raw_unicode_escape')
	k2 = key[1].encode('raw_unicode_escape')
	k3 = key[5].encode('raw_unicode_escape')
	k4 = key[7].encode('raw_unicode_escape')
	k5 = key[8].encode('raw_unicode_escape')
	k6 = key[9].encode('raw_unicode_escape')
	k7 = key[10].encode('raw_unicode_escape')
	k8 = key[11].encode('raw_unicode_escape')
	k9 = key[12].encode('raw_unicode_escape')
	k10 = key[16].encode('raw_unicode_escape')
	lastresult.append({"businesscode":k1,"businessname":k2,"businessmanager":k3,"Monday":k4,"Tuesday":k5,"Wednesday":k6,"Thursday":k7,"Friday":k8,"Judge":k9,"remark":k10})



print("Content-type: text/html\n")

print(lastresult)

