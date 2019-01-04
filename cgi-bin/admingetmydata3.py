#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select NAME , EMAIL from WORKER')
username = cu.fetchall()
newname = []
for key in username:
	name = key[0].encode('raw_unicode_escape')
	email = key[1].encode('raw_unicode_escape')
	newname.append({"email":email,"name":name})


print("Content-type: text/html\n")

print(newname)


 
