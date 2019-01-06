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



def mail():
    ret=True
    try:
        msg=MIMEText(str(username)+'通过了您在'+str(mondaytime)+"这一周的"+str(businesscode)+"项目的工时提交",'plain','utf-8')
        msg['From']=formataddr(["库柏特项目工时管理系统",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="项目工时通过" #邮件的主题，也可以说是标题
        server=smtplib.SMTP("220.181.12.14",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret

ret=mail()


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
