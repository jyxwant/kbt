#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests


form = cgi.FieldStorage()
email = form.getvalue('email')
password = form.getvalue('password')
name = form.getvalue('name')
oldname = form.getvalue('oldname')

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('INSERT INTO WORKER VALUES ("%s","%s","%s" );'%(email,password,name))
db.commit()
db.close()



print("Content-type: text/html\n")

print(email)
