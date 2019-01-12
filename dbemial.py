#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import smtplib
import email.MIMEMultipart
import email.MIMEText
import email.MIMEBase
import os.path
import time
from email.mime.text import MIMEText
from email.utils import formataddr

import sys
reload(sys)
sys.setdefaultencoding('utf8')




while(True):
	From = "cobotsys2019@163.com"
	To = "j1132346005@163.com"
	file_name = "./database/kbt.db"
	server=smtplib.SMTP_SSL("smtp.163.com",465)
	server.login("cobotsys2019@163.com","cobot2019")
	main_msg = email.MIMEMultipart.MIMEMultipart()
	text_msg = email.MIMEText.MIMEText("")
	main_msg.attach(text_msg)
	contype = 'application/octet-stream'
	maintype, subtype = contype.split('/', 1)
	data = open(file_name, 'rb')
	file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
	file_msg.set_payload(data.read( ))
	data.close( )
	email.Encoders.encode_base64(file_msg)
	basename = os.path.basename(file_name)
	file_msg.add_header('Content-Disposition',
	 'attachment', filename = basename)
	main_msg.attach(file_msg)
	main_msg['From']=formataddr([u"库柏特项目工时管理系统数据库备份".encode('utf-8'),From])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
	main_msg['To']=formataddr(["coboter",To])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
	main_msg['Subject'] = u"库柏特项目工时管理系统数据库备份".encode('utf-8')
	main_msg['Date'] = email.Utils.formatdate( )
	fullText = main_msg.as_string( )
	try:
		server.sendmail(From, To, fullText)
	finally:
		server.quit()

	time.sleep(24*3600)

