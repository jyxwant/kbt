#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests
import datetime
from datetime import timedelta
import sys
if sys.getdefaultencoding() != 'utf-8':
	reload(sys)
	sys.setdefaultencoding('utf-8')
form = cgi.FieldStorage() 

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select PROJECTMANAGER,PROJECTWORKER,PROJECTID,PROJECTNAME,MONDAYTIME from WORK where JUDGE="未审批"')
username = cu.fetchall()
newname = []
for key in username:
	businessmanager = key[0].encode('raw_unicode_escape')
	businessworker = key[1].encode('raw_unicode_escape')
	businesscode = key[2].encode('raw_unicode_escape')
	businessname = key[3].encode('raw_unicode_escape')
	mondaytime = key[4].encode('raw_unicode_escape')
	newname.append({"businessmanager":businessmanager,"businessworker":businessworker,"businesscode":businesscode,"businessname":businessname,"mondaytime":mondaytime})

print("Content-type: text/html\n")

print(newname)

