#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests


form = cgi.FieldStorage()

businesscode = form.getvalue('businesscode')
username = form.getvalue('username')
mondaytime  = form.getvalue('mondaytime')

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('DELETE FROM WORK WHERE PROJECTID = "%s" and PROJECTWORKER = "%s" and MONDAYTIME = "%s";'%(businesscode,username,mondaytime))
db.commit()
db.close()




print("Content-type: text/html\n")

print(mondaytime)

