#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests

form = cgi.FieldStorage()
source = form.getvalue('source')
thenew = form.getvalue('thenew')
email  = form.getvalue('email')


db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute("select * from WORKER where EMAIL = '%s' and PASSWORD = '%s'"%(email,source))
result = cu.fetchall()
last = "原密码错误"
if result != []:
	cu.execute("update WORKER set PASSWORD='%s' WHERE EMAIL = '%s'"%(thenew,email))
	last = "修改完成"
db.commit()
db.close()

print("Content-type: text/html\n")
print(last)
