#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select * from WORKER')

result = cu.fetchall()


#转换为json
lastresult = []
for key in result:
	k1 = key[0].encode('raw_unicode_escape')
	k2 = key[1].encode('raw_unicode_escape')
	k3 = key[2].encode('raw_unicode_escape')
	lastresult.append({"emailname":k1,"password":k2,"Name":k3})



print("Content-type: text/html\n")

print(lastresult)

