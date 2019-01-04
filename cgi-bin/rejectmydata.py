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
cu.execute('update WORK set JUDGE = "审批拒绝" where PROJECTWORKER = "%s" and MONDAYTIME = "%s" and PROJECTMANAGER = "%s" and PROJECTID = "%s" '%(businessman,mondaytime,username,businesscode))
db.commit()
db.close()



print("Content-type: text/html\n")

print(mondaytime)
