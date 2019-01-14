#!/usr/bin/python2
# -*- coding: UTF-8 -*-


#每天从BUSINESS检查项目,看是否到期，看是否超标，如果还剩一周，每天提醒。

import sqlite3 
import datetime
from datetime import timedelta
import time
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr

"""

my_sender='j1132346005@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='liaoshenghua@cobotsys.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
def mail():
    ret=True
    try:
        msg=MIMEText('这是一封测试的邮件','plain','utf-8')
        msg['From']=formataddr(["cobot",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["liaoshenghua@cobotsys.com",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="test" #邮件的主题，也可以说是标题
        server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"j1132346005")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret

ret=mail()
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  #如果发送失败则会返回filed


"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')







def mail1():
    ret=True

    try:
        msg=MIMEText(str(username)+"提交了"+str(mondaytime)+"这一周的"+str(businesscode)+"-"+businessname+"项目的工时",'plain','utf-8')
        msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=u"项目工时提交".encode('utf-8') #邮件的主题，也可以说是标题
        server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送
        server.quit()   #这句是关闭连接的意思

    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret


def mail2():
    ret=True

    try:
        msg=MIMEText(str(username)+"删除了"+str(mondaytime)+"这一周的"+str(businesscode)+"-"+businessname+"项目的工时",'plain','utf-8')
        msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=u"项目工时删除".encode('utf-8') #邮件的主题，也可以说是标题
        server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送
        server.quit()   #这句是关闭连接的意思

    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret


def mail3():
    ret=True

    try:
        msg=MIMEText(str(username)+"同意了"+str(mondaytime)+"这一周的"+str(businesscode)+"-"+businessname+"项目的工时"+"   备注："+remark,'plain','utf-8')
        msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=u"项目工时审批通过".encode('utf-8') #邮件的主题，也可以说是标题
        server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送
        server.quit()   #这句是关闭连接的意思

    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret


def mail4():
    ret=True

    try:
        msg=MIMEText(str(username)+"拒绝了"+str(mondaytime)+"这一周的"+str(businesscode)+"-"+businessname+"项目的工时"+"   备注："+remark,'plain','utf-8')
        msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=u"项目工时审批拒绝".encode('utf-8') #邮件的主题，也可以说是标题
        server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送
        server.quit()   #这句是关闭连接的意思

    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret


my_sender='cobotsys2019@163.com'
while(True):
    now = datetime.datetime.now()
    db = sqlite3.connect('./database/kbt.db')
    cu   = db.cursor()
    cu.execute('select * from EMAIL')
    result = cu.fetchall()
    for key in result:
        if key[5] == '1':
            username = key[0]
            receivename = key[1]
            mondaytime = key[4]
            my_user = key[2]
            businesscode = key[3]
            businessname = key[6]
            cu.execute('DELETE FROM EMAIL WHERE  SENDNAME= "%s" and RECEIVENAME = "%s" and SENDMAIL="%s" and BUSINESSCODE = "%s" and BEHAVE="1" and MONDAYTIME = "%s";'\
                %(username,receivename,my_user,businesscode,mondaytime))
            my_user = str(my_user)
            print "hello"
            ret = mail1()
            print ret
            db.commit()
    for key in result:
        if key[5] == '2':
            username = key[0]
            receivename = key[1]
            mondaytime = key[4]
            my_user = key[2]
            businesscode = key[3]
            businessname = key[6]
            cu.execute('DELETE FROM EMAIL WHERE  SENDNAME= "%s" and RECEIVENAME = "%s" and SENDMAIL="%s" and BUSINESSCODE = "%s" and BEHAVE="2" and MONDAYTIME = "%s";'\
                %(username,receivename,my_user,businesscode,mondaytime))
            my_user = str(my_user)
            mail2()
            db.commit()
    for key in result:
        if key[5] == '3':
            username = key[0]
            receivename = key[1]
            mondaytime = key[4]
            my_user = key[2]
            businesscode = key[3]
            businessname = key[6]
            remark = key[7]
            cu.execute('DELETE FROM EMAIL WHERE  SENDNAME= "%s" and RECEIVENAME = "%s" and SENDMAIL="%s" and BUSINESSCODE = "%s" and BEHAVE="3" and MONDAYTIME = "%s";'\
                %(username,receivename,my_user,businesscode,mondaytime))
            my_user = str(my_user)
            mail3()
            db.commit()
    for key in result:
        if key[5] == '4':
            username = key[0]
            receivename = key[1]
            mondaytime = key[4]
            my_user = key[2]
            businesscode = key[3]
            businessname = key[6]
            remark = key[7]
            cu.execute('DELETE FROM EMAIL WHERE  SENDNAME= "%s" and RECEIVENAME = "%s" and SENDMAIL="%s" and BUSINESSCODE = "%s" and BEHAVE="4" and MONDAYTIME = "%s";'\
                %(username,receivename,my_user,businesscode,mondaytime))
            my_user = str(my_user)
            mail4()
            db.commit()
    db.commit()
    db.close()
    time.sleep(60*3)

