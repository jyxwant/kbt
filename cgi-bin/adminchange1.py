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


#更新WORKER表中的用户名和密码数据，将BUSINESS和WORK中的姓名替换成新编辑的姓名
db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('update WORKER set EMAIL="%s",NAME = "%s",PASSWORD = "%s" where  EMAIL= "%s"'%(email,name,password,email))
cu.execute('update BUSINESS set BUSINESSWORKER =replace(BUSINESSWORKER,"%s","%s")'%(oldname,name))
cu.execute('update BUSINESS set BUSINESSMANAGER =replace(BUSINESSMANAGER,"%s","%s")'%(oldname,name))
cu.execute('update WORK set PROJECTWORKER =replace(PROJECTWORKER,"%s","%s")'%(oldname,name))
cu.execute('update WORK set PROJECTMANAGER =replace(PROJECTMANAGER,"%s","%s")'%(oldname,name))

db.commit()


db.close()



print("Content-type: text/html\n")

print(name)
