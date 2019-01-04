#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests

db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select EMAIL from WORKER')
username = cu.fetchall()



print("Content-type: text/html\n")

print(username)


 
