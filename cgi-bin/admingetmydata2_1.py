#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select * from BUSINESS')

result = cu.fetchall()

onlyone = []
lastresult = []
for key in result:
	k1 = key[0].encode('raw_unicode_escape')
	k2 = key[1].encode('raw_unicode_escape')
	k3 = key[2].encode('raw_unicode_escape')
	k4 = key[10].encode('raw_unicode_escape')
	k5 = key[3].encode('raw_unicode_escape')
	k6 = key[4].encode('raw_unicode_escape')
	k7 = key[5].encode('raw_unicode_escape')
	k8 = key[6].encode('raw_unicode_escape')
	k9 = key[7].encode('raw_unicode_escape')
	k10 = key[8].encode('raw_unicode_escape')
	k11 = key[9].encode('raw_unicode_escape')
	lastresult.append({"businesscode":k1,"businessname":k2,"businessmanager":k3,"status":k4,"now":k5,"businessworker":k6,"workertime":k7,"beyond":k8,"start":k9,"end":k10,"should":k11})
#转换为json




print("Content-type: text/html\n")

print(lastresult)


 
