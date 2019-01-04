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
monday = form.getvalue('monday')
tuesday = form.getvalue('tuesday')
wednesday = form.getvalue('wednesday')
thursday = form.getvalue('thursday')
friday = form.getvalue('friday')

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('update WORK set MONDAY = "%s", TUESDAY="%s", WEDNESDAY="%s",THURSDAY="%s",FRIDAY="%s" where PROJECTID="%s" and PROJECTWORKER="%s" and MONDAYTIME="%s"'%(monday,tuesday,wednesday,thursday,friday,businesscode,username,mondaytime))
db.commit()
db.close()






print("Content-type: text/html\n")

print(mondaytime)
