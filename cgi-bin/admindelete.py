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
email = form.getvalue('emailname')
name = form.getvalue('name')
cu.execute('DELETE FROM WORKER WHERE EMAIL="%s";'%(email))
cu.execute('DELETE FROM WORK WHERE (PROJECTWORKER="%s" OR PROJECTMANAGER="%s") and (JUDGE="" OR JUDGE="");'%(name,name))
db.commit()
db.close()


print("Content-type: text/html\n")

print(email)