#!/usr/bin/python2
# -*- coding: UTF-8 -*-



#后台任务，每周一添加work表格，一行，其中若项目为激活状态，增加一行JUDGE为none，项目人员为none的一行。
#每周一除了添加一个JUDGE为none的行外还要添加上一周参加某一项目的人员这一周的初始项目

import sqlite3 
import datetime
from datetime import timedelta
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')

while(True):
	now = datetime.datetime.now()
	if now.weekday() == 5:
		monday = now - timedelta(days=now.weekday())
		lastmonday = now - timedelta(days=now.weekday() + 7)
		monday = str(monday.year) + '-' + str(monday.month).zfill(2) + '-' + str(monday.day).zfill(2)
		lastmonday = str(lastmonday.year) + '-' + str(lastmonday.month).zfill(2) + '-' + str(lastmonday.day).zfill(2)
		db   = sqlite3.connect('./database/kbt.db')
		cu   = db.cursor()
		cu.execute('select * from BUSINESS WHERE STATUS == "激活"')
		result = cu.fetchall()
		#for循环，使提取的每个项目编码只有一列
		onlyone = []
		theonly = []
		for key in result:
			if key[0] in onlyone:
				continue
			else:
				k1 = key[0]
				k2 = key[1]
				k3 = key[2]
				k4 = key[3]
				k5 = key[7]
				k6 = key[8]
				k7 = key[9]
				theonly.append({"businesscode":k1,"businessname":k2,"businessmanager":k3,\
					"now":k4,"starttime":k5,"endtime":k6,"should":k7})
				onlyone.append(k1)
		for key in theonly:
			ratio = str(key['now']) + '/' + str(key['should'])
			cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","%s","%s","%s","none","0","0","0","0","0","none","%s","%s","%s")'\
				%(key['businesscode'],key['businessname'],key['starttime'],key['should'],ratio,key['businessmanager'],key['now'],key['endtime'],monday))
		#for循环，直接更新work表格
		for key in onlyone:
			print key
			cu.execute('select * from WORK where JUDGE!="none" and PROJECTID="%s" and MONDAYTIME="%s"'%(key,lastmonday))
			newresult = cu.fetchall()
			print newresult
			for newkey in newresult:
				k1 = newkey[0] 
				k2 = newkey[1]
				k3 = newkey[2]
				k4 = newkey[3]
				k5 = newkey[4]
				k6 = newkey[5]
				k7 = newkey[6]
				k8 = newkey[13]
				k9 = newkey[14]
				cu.execute('INSERT INTO WORK VALUES("%s","%s","%s","%s","%s","%s","%s","0","0","0","0","0","未审批","%s","%s","%s")'\
					%(k1,k2,k3,k4,k5,k6,k7,k8,k9,monday))
		db.commit()
		db.close()
	time.sleep(24*3600)
