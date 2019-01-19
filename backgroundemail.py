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


def mail():
	ret=True
	try:
		msg=MIMEText("coboter您好：注意提交和审批工时^_^",'plain','utf-8')
		msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
		msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject']=u"请注意提交和审批本周工时，如果已提交请忽略".encode('utf-8') #邮件的主题，也可以说是标题
		server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
		server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
		server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()   #这句是关闭连接的意思
	except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
		ret=False
	return ret

def mail1():
	ret=True
	print "mail1"
	try:
		msg=MIMEText("coboter您好：距离项目"+thebusiness+"-"+businessname+"截止还有"+str(days)+"天,但是工时尚未满足要求",'plain','utf-8')
		msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
		msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject']=u"项目进度提醒".encode('utf-8') #邮件的主题，也可以说是标题
		server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
		server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
		server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()   #这句是关闭连接的意思
	except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
		ret=False
	print ret
	return ret




#额外收到邮件的人
def mail2():
	ret=True
	print "mail1"
	try:
		my_user = "liaoshenghua@cobotsys.com"   #####!!!!!!!!改这里
		msg=MIMEText("廖总您好：距离项目"+thebusiness+"-"+businessname+"截止还有"+str(days)+"天,但是工时尚未满足要求",'plain','utf-8')
		msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
		msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject']=u"项目进度提醒".encode('utf-8') #邮件的主题，也可以说是标题
		server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
		server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
		server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()   #这句是关闭连接的意思
	except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
		ret=False
	print ret
	return ret

#额外收到邮件的人
def mail3():
	ret=True
	print "mail1"
	try:######  ########
		my_user = ""   #####!!!!!!!!改这里
		msg=MIMEText("coboter您好：距离项目"+thebusiness+"-"+businessname+"截止还有"+str(days)+"天,但是工时尚未满足要求",'plain','utf-8')
		msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
		msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject']=u"项目进度提醒".encode('utf-8') #邮件的主题，也可以说是标题
		server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
		server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
		server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()   #这句是关闭连接的意思
	except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
		ret=False
	print ret
	return ret


#额外收到邮件的人
def mail4():
	ret=True
	print "mail1"
	try:
		my_user = ""   #####!!!!!!!!改这里
		msg=MIMEText("coboter您好：距离项目"+thebusiness+"-"+businessname+"截止还有"+str(days)+"天,但是工时尚未满足要求",'plain','utf-8')
		msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
		msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject']=u"项目进度提醒".encode('utf-8') #邮件的主题，也可以说是标题
		server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
		server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
		server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()   #这句是关闭连接的意思
	except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
		ret=False
	print ret
	return ret


#额外收到邮件的人
def mail5():
	ret=True
	print "mail1"
	try:
		my_user = ""   #####!!!!!!!!改这里
		msg=MIMEText("coboter您好：距离项目"+thebusiness+"-"+businessname+"截止还有"+str(days)+"天,但是工时尚未满足要求",'plain','utf-8')
		msg['From']=formataddr([u"库柏特项目工时管理系统".encode('utf-8'),my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
		msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject']=u"项目进度提醒".encode('utf-8') #邮件的主题，也可以说是标题
		server=smtplib.SMTP_SSL("smtp.163.com",465)  #发件人邮箱中的SMTP服务器，端口是25
		server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
		server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()   #这句是关闭连接的意思
	except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
		ret=False
	print ret
	return ret




while (True):
	now = datetime.datetime.now()
	time.sleep(1800)
	if now.hour == 3:
		break

my_sender='cobotsys2019@163.com'

while(True):
	now = datetime.datetime.now()
	db = sqlite3.connect('./database/kbt.db')
	cu   = db.cursor()
	cu.execute('select * from BUSINESS where BEYOND = "否"')
	result = cu.fetchall()
	theonly = []
	for key in result:
		lastday = datetime.datetime.strptime(str(key[8]), "%Y-%m-%d")
		days = lastday - now
		days = days.days
		print days
		if days <= 21:
			print "ok"
			cu.execute('select * from WORKER')
			newresult = cu.fetchall()
			for key1 in newresult:
				my_user = str(key1[0])
				thebusiness = str(key[0])
				businessname = str(key[1])
				print thebusiness
				print my_user
				ret = mail1()
				ret = mail2()
				#ret = mail3()
				#ret = mail4()
				#ret = mail5()
				break
	if now.weekday() == 4:
		cu.execute('select * from WORKER')
		result = cu.fetchall()
		for key in result:
			my_user = str(key[0])
			mail()
	db.commit()
	db.close()
	time.sleep(24*3600)

