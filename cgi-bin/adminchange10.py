#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests


form = cgi.FieldStorage()
email = form.getvalue('email')
password = form.getvalue('password')
name = form.getvalue('name')



#从数据库中获取原用户名，方便接下来的数据库操作
db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select * from WORKER where EMAIL="%s" and PASSWORD="%s"'%(email,password))

result = cu.fetchall()

lastresult = []

for key in result:
	k1 = key[2].encode('raw_unicode_escape')
	lastresult.append({"name":k1})
	break

print("Content-type: text/html\n")

print(lastresult)
