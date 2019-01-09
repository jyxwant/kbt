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
businessmanager = form.getvalue('businessmanager')


db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()

cu.execute('select * from WORKER WHERE NAME="%s"'%(businessmanager))
emailresult = cu.fetchall()
for key in emailresult:
    my_sender=str('cobotsys2019@163.com') #发件人邮箱账号，为了后面易于维护，所以写成了变量
    my_user= str(key[0]) #收件人邮箱账号，为了后面易于维护，所以写成了变量
    break
cu.execute('INSERT INTO EMAIL VALUES ("%s","%s","%s","%s","%s","2");'%(username,businessmanager,my_user,businesscode,mondaytime))

cu.execute('DELETE FROM WORK WHERE PROJECTID = "%s" and PROJECTWORKER = "%s" and MONDAYTIME = "%s";'%(businesscode,username,mondaytime))
db.commit()
db.close()




print("Content-type: text/html\n")

print(mondaytime)

