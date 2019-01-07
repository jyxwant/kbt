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


import sys
reload(sys)
sys.setdefaultencoding('utf8')


def mail():
	ret=True
	try:
		msg=MIMEText("coboter您好：注意提交和审批工时^_^",'plain','utf-8')
		print "1"
		msg['From']=formataddr(["库柏特项目工时管理系统",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
		print "2"
		msg['To']=formataddr(["coboter",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
		print "3"
		msg['Subject']="请注意提交和审批工时" #邮件的主题，也可以说是标题
		print "4"
		server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
		print "5"
		server.login(my_sender,"cobot2019")    #括号中对应的是发件人邮箱账号、邮箱密码
		print "6"
		server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		print "7"
		server.quit()   #这句是关闭连接的意思
	except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
		ret=False
	return ret




"""

while (True):
	now = datetime.datetime.now()
	time.sleep(1800)
	if now.hour == 3:
		break
"""
my_sender='cobotsys2019@163.com'
my_user = 'j1132346005@163.com'
mail()



"""
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
				print thebusiness
				print my_user
				ret = mail1()
				#ret = mail2()
				#ret = mail3()
				#ret = mail4()
				#ret = mail5()
				break
	if now.weekday() == 2:
		cu.execute('select * from WORKER')
		result = cu.fetchall()
		for key in result:
			my_user = str(key[0])
			time.sleep(20)
			ret = mail()
			print my_user
			print ret
	if now.weekday() == 4:
		cu.execute('select * from WORKER')
		result = cu.fetchall()
		for key in result:
			my_user = str(key[0])
			mail()
	db.commit()
	db.close()
	time.sleep(24*3600)
"""

