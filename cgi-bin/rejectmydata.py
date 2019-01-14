#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests

import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr

form = cgi.FieldStorage()
username = form.getvalue('username')
businesscode = form.getvalue('businesscode')
businessman = form.getvalue('businessman')
mondaytime  = form.getvalue('mondaytime')
businessname = form.getvalue('businessname')


db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select * from WORKER WHERE NAME="%s"'%(businessman))
emailresult = cu.fetchall()
for key in emailresult:
    my_sender=str('cobotsys2019@163.com') #发件人邮箱账号，为了后面易于维护，所以写成了变量
    my_user= str(key[0]) #收件人邮箱账号，为了后面易于维护，所以写成了变量
    break
cu.execute('INSERT INTO EMAIL VALUES ("%s","%s","%s","%s","%s","4","%s");'%(username,businessman,my_user,businesscode,mondaytime,businessname))


cu.execute('update WORK set JUDGE = "审批拒绝" where PROJECTWORKER = "%s" and MONDAYTIME = "%s" and PROJECTMANAGER = "%s" and PROJECTID = "%s" '%(businessman,mondaytime,username,businesscode))
db.commit()
db.close()



print("Content-type: text/html\n")

print(mondaytime)
