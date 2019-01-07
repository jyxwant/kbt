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



db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('select * from WORKER WHERE NAME="%s"'%(businessman))
emailresult = cu.fetchall()
for key in emailresult:
    my_sender=str('cobotsys2019@163.com') #发件人邮箱账号，为了后面易于维护，所以写成了变量
    my_user= str(key[0]) #收件人邮箱账号，为了后面易于维护，所以写成了变量
    break
def mail():
    ret=True
    try:
        msg=MIMEText(str(username)+'拒绝了您在'+str(mondaytime)+"这一周的"+str(businesscode)+"项目的工时提交",'plain','utf-8')
        msg['From']=formataddr(["库柏特项目工时管理系统",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="项目工时拒绝" #邮件的主题，也可以说是标题
        server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret

ret=mail()

cu.execute('update WORK set JUDGE = "审批拒绝" where PROJECTWORKER = "%s" and MONDAYTIME = "%s" and PROJECTMANAGER = "%s" and PROJECTID = "%s" '%(businessman,mondaytime,username,businesscode))
db.commit()
db.close()



print("Content-type: text/html\n")

print(mondaytime)
