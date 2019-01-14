#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests

#email
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr

form = cgi.FieldStorage()
username = form.getvalue('username')
businesscode = form.getvalue('businesscode')
businessman = form.getvalue('businessman')
mondaytime  = form.getvalue('mondaytime')
total = form.getvalue('total')
now1 = form.getvalue('nonedone')
businessname = form.getvalue('businessname')
workertime = form.getvalue('workertime')
start = form.getvalue('starttime')
end = form.getvalue('endtime')
should = form.getvalue('should')
status = form.getvalue('status')



now1 = int(now1) + int(total)
workertime = int(workertime) + int(total)
beyond = "否"
if now1 > int(should):
	beyond = "是"

ratio = str(now1) + '/' + should


db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select * from WORKER WHERE NAME="%s"'%(businessman))
emailresult = cu.fetchall()
for key in emailresult:
    my_sender=str('cobotsys2019@163.com') #发件人邮箱账号，为了后面易于维护，所以写成了变量
    my_user= str(key[0]) #收件人邮箱账号，为了后面易于维护，所以写成了变量
    break

cu.execute('INSERT INTO EMAIL VALUES ("%s","%s","%s","%s","%s","3","%s");'%(username,businessman,my_user,businesscode,mondaytime,businessname))
cu.execute('update WORK set JUDGE="审批通过" where PROJECTWORKER="%s" and MONDAYTIME="%s" and PROJECTMANAGER="%s" and PROJECTID="%s" '%(businessman,mondaytime,username,businesscode))
db.commit()
cu.execute('select * FROM BUSINESS where BUSINESSCODE="%s" and BUSINESSWORKER="%s"'%(businesscode,businessman))
result = cu.fetchall()
if result == []:
    cu.execute('INSERT INTO BUSINESS VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");'\
        %(businesscode,businessname,username,now1,businessman,workertime,beyond,start,end,should,status))
    db.commit()
else:
    cu.execute('update BUSINESS set BEYOND = "%s", WORKERTIME="%s", NOW="%s" where BUSINESSCODE="%s" and BUSINESSWORKER="%s"'%(beyond,workertime,now1,businesscode,businessman))
    db.commit()
cu.execute('select * FROM BUSINESS where BUSINESSCODE="%s" and BUSINESSWORKER="none"'%(businesscode))
result = cu.fetchall()

if result != []:
    cu.execute('DELETE FROM BUSINESS where BUSINESSCODE="%s" and BUSINESSWORKER="none"'%(businesscode))
    db.commit()

cu.execute('update WORK set RATIO = "%s" where PROJECTID="%s"'%(ratio,businesscode))
db.commit()

db.close()





print("Content-type: text/html\n")

print(ret)
