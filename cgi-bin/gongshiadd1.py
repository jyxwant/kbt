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
businessname = form.getvalue('businessname')
starttime = form.getvalue('starttime')
done = form.getvalue('done')
ratio = form.getvalue('ratio')
businessmanager = form.getvalue('businessmanager')
now = form.getvalue('now')
endtime = form.getvalue('endtime')




db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","%s","%s","%s","%s","0","0","0","0","0","未审批","%s","%s","%s");'\
	%(businesscode,businessname,starttime,done,ratio,businessmanager,username,now,endtime,mondaytime))
db.commit()
db.close()

print("Content-type: text/html\n")

print(username)
