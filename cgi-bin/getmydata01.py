#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests


form = cgi.FieldStorage()


username = form.getvalue('username')
mondaytime  = form.getvalue('mondaytime')

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select PROJECTID,PROJECTNAME,PROJECTMANAGER from WORK where  PROJECTWORKER!="%s" and MONDAYTIME="%s" and JUDGE = "none"'%(username,mondaytime))
result = cu.fetchall()


lastresult = []
for key in result:
	k1 = key[0].encode('raw_unicode_escape')
	k2 = key[1].encode('raw_unicode_escape')
	k3 = key[2].encode('raw_unicode_escape')
	lastresult.append({"businesscode":k1,"businessname":k2,"businessmanager":k3})



print("Content-type: text/html\n")

print(lastresult)