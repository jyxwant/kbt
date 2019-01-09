#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import cgi, cgitb 
import sqlite3 
import datetime
from datetime import timedelta
form = cgi.FieldStorage() 
# 获取数据
site_email = form.getvalue('username')
site_password  = form.getvalue('pwd')
# 创建 FieldStorage 的实例化
db   = sqlite3.connect('../database/kbt.db')
cu   = db.cursor()
cu.execute('SELECT NAME FROM WORKER WHERE EMAIL = "%s" AND PASSWORD = "%s"'%(site_email,site_password))
username = cu.fetchall()
thisname = username[0][0].encode('utf-8')
thisname.decode('utf8').encode('gb2312')
#获取时间
now = datetime.datetime.now()

monday = now - timedelta(days=now.weekday() + 21)
mondaytime = str(monday.year) + '-' + str(monday.month).zfill(2) + '-' + str(monday.day).zfill(2)
getstart = str(monday.year) + '-' + str(monday.month).zfill(2) + '-' + str(monday.day).zfill(2)
monday =  str(monday.month).zfill(2) + '/' + str(monday.day).zfill(2)
tuesday = now - timedelta(days=(now.weekday() + 20))
tuesday =  str(tuesday.month).zfill(2) + '/' + str(tuesday.day).zfill(2)
wednesday = now - timedelta(days=now.weekday() + 19)
wednesday =  str(wednesday.month).zfill(2) + '/' + str(wednesday.day).zfill(2)
thursday = now - timedelta(days=now.weekday() + 18)
thursday =  str(thursday.month).zfill(2) + '/' + str(thursday.day).zfill(2)
friday = now - timedelta(days=now.weekday() + 17)
getend = str(friday.year) + '-' + str(friday.month).zfill(2) + '-' + str(friday.day).zfill(2)
friday = str(friday.month).zfill(2) + '/' + str(friday.day).zfill(2)
last_zero_monday =  now - timedelta(days=now.weekday())
last_zero_friday = now - timedelta(days=(now.weekday() - 4))
last_zero = '本周' + '(' + str(last_zero_monday.month).zfill(2) + '/' + str(last_zero_monday.day).zfill(2) + '-' +  \
str(last_zero_friday.month).zfill(2) + '/' + str(last_zero_friday.day).zfill(2) + ')'
last_one_monday = now - timedelta(days=(now.weekday() + 7))
last_one_friday = now - timedelta(days=(now.weekday() + 3))
last_one = '上一周' + '(' + str(last_one_monday.month).zfill(2) + '/' + str(last_one_monday.day).zfill(2) + '-' +  \
str(last_one_friday.month).zfill(2) + '/' + str(last_one_friday.day).zfill(2) + ')'
last_two_monday = now - timedelta(days=(now.weekday() + 14))
last_two_friday = now - timedelta(days=(now.weekday() + 10))
last_two = '上两周' + '(' + str(last_two_monday.month).zfill(2) + '/' + str(last_two_monday.day).zfill(2) + '-' +  \
str(last_two_friday.month).zfill(2) + '/' + str(last_two_friday.day).zfill(2) + ')'
last_three_monday = now - timedelta(days=(now.weekday() + 21))
last_three_friday = now - timedelta(days=(now.weekday() + 17))
last_three = '上三周' + '(' + str(last_three_monday.month).zfill(2) + '/' + str(last_three_monday.day).zfill(2) + '-' +  \
str(last_three_friday.month).zfill(2) + '/' + str(last_three_friday.day).zfill(2) + ')'
last_four_monday = now - timedelta(days=(now.weekday() + 28))
last_four_friday = now - timedelta(days=(now.weekday() + 24))
last_four = '上四周' + '(' + str(last_four_monday.month).zfill(2) + '/' + str(last_four_monday.day).zfill(2) + '-' +  \
str(last_four_friday.month).zfill(2) + '/' + str(last_four_friday.day).zfill(2) + ')'



#获取数据
print "Content-type:text/html"
print
if username != []:
  print "<!DOCTYPE html>"
  print "<html>"
  print "<head>"
  print "  <meta charset='utf-8'>"
  print "  <meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1'>"
  print "    <meta http-equiv='content-language' content='zh-CN' />"
  print "  <title>项目工时管理系统</title>"
  print "  <link rel='stylesheet' href='../layui/css/layui.css'>"
  print "  <link rel='stylesheet' href='../css/mycss.css'>"
  print "</head>"
  print "<body class='layui-layout-body'>"
  print "<form method='post' action='waitforme1.py' style='display:none;'>"
  print "<input name='username' value=%s class='ur' />"%(site_email)
  print "<input name='pwd' value=%s class='pw' />"%(site_password)
  print "<input name='thisname' value=%s class='pw' />"%(thisname)
  print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'waitforme' /></div>"
  print "</form>"
  print "<form method='post' action='changepassword.py' style='display:none;'>"
  print "<input name='username' value=%s class='ur' />"%(site_email)
  print "<input name='pwd' value=%s class='pw' />"%(site_password)
  print "<input name='thisname' value=%s class='pw' />"%(thisname)
  print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'changepwd' /></div>"
  print "</form>"
  print "<div class='layui-layout layui-layout-admin'>"
  print "<div id = 'monday' style='display:none;'>%s</div>"%(monday)
  print "<div id = 'tuesday' style='display:none;'>%s</div>"%(tuesday)
  print "<div id = 'wednesday' style='display:none;'>%s</div>"%(wednesday)
  print "<div id = 'thursday' style='display:none;'>%s</div>"%(thursday)
  print "<div id = 'friday' style='display:none;'>%s</div>"%(friday)
  print "<div id = 'username' style='display:none;'>%s</div>"%(thisname)
  print "<div id = 'getstart' style='display:none;'>%s</div>"%(getstart)
  print "<div id = 'getend' style='display:none;'>%s</div>"%(getend)
  print "<div id = 'mondaytime' style='display:none;'>%s</div>"%(mondaytime)
  
  print "  <div class='layui-header'>   "
  print "   <!-- 头部区域（可配合layui已有的水平导航） -->"
  print "    <ul class='layui-nav'>"
  print "      <li class='layui-nav-item layui-this'><a href='#' onclick='location.reload();'>工时填写</a></li>"
  print "      <li class='layui-nav-item'><a href='#' onclick='wait()'>待我审批的工时</a></li>"
  print "      <li class='layui-nav-item'><a href='#' onclick='changepassword()'>修改密码</a></li> "
  print "    </ul>"
  print "    <ul class='layui-nav layui-layout-right'>"
  print "      <li class='layui-nav-item'><a href='#'>%s</a></li><!--python-->"%(site_email)
  print "    </ul>"
  print "  </div>"
  
  
  print "  <div >"
  print "    <!-- 内容主体区域 -->"
  print "    <div style='padding: 8px;padding-top:0px;'>"



  print "    "
  print "      <div class='layui-row' style='padding: 0px;    padding-buttom:0px;'>"
  print "     "
  print "        <div class='layui-col-md5'>"
  print "          <form class='layui-form' action=''>"
  print "          "
  print "            <select name='city'  lay-verify='' id='#selected' lay-filter='choseweek'>"
  print "                <option value='' >%s</option>"%(last_three)
  print "              <option value='0' >%s</option>"%(last_zero)
  print "                <option value='1' >%s</option>"%(last_one)
  print "               <option value='2'>%s</option>"%(last_two)
  print "                <option value='3' selected>%s</option>"%(last_three)
  print "                <option value='4'>%s</option>"%(last_four)
  print "            </select>"

  print "          </form>"
  print "        </div>"

  print "      <div class='layui-col-md7'>"
  print "      </div>"

  print "    </div>"


  print "    <div class='layui-row' style='padding:0px;'>"
  print "      <div class='layui-col-md12' style='margin-bottom:40px'>"

  print "        <table id='demo' lay-filter='test'></table>"

  print "      </div>"

  print "      <div class='layui-row' >"
  print "        <button class='layui-btn' id='addRow'>添加我所参与的项目</button>"
  print "        <button class='layui-btn' id='delRow'>删除我所选中的项目</button>"
  print "        <button class='layui-btn' id='add' onclick='commitmydata()'>提交工时</button>"
  print "      </div>"
  print "      <p>填表说明<p>"
  print "      <p>1.如果数据没有出来，请刷新一下<p>"
  print "      <p>2.您的每天的总工时不能超过8小时<p>"
  print "      <p>3.如果您在周六或者周日工作，请与项目经理沟通后折算到周一到周五<p>"
  print "      <p>4.表格中只会显示审批通过的和未审批的数据，其中未审批的数据可以修改和删除</p>"
  print "    </div>"
  print "  </div>"
  
  print "  <div class='layui-footer'>"
  print "    <!-- 底部固定区域 -->"
  print "    © 武汉库柏特科技有限公司-项目工时管理系统"
  print "  </div>"
  print "</div>"
  print "<body class='layui-layout-body'>"



  print "<form method='post' action='kbt1.py' style='display:none;'>"
  print "<input name='username' value=%s class='ur' />"%(site_email)
  print "<input name='pwd' value=%s class='pw' />"%(site_password)
  print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'kbt1' /></div>"
  print "</form>"


  print "<form method='post' action='kbt2.py' style='display:none;'>"
  print "<input name='username' value=%s class='ur' />"%(site_email)
  print "<input name='pwd' value=%s class='pw' />"%(site_password)
  print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'kbt2' /></div>"
  print "</form>"

  print "<form method='post' action='kbt3.py' style='display:none;'>"
  print "<input name='username' value=%s class='ur' />"%(site_email)
  print "<input name='pwd' value=%s class='pw' />"%(site_password)
  print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'kbt3' /></div>"
  print "</form>"


  print "<form method='post' action='kbt4.py' style='display:none;'>"
  print "<input name='username' value=%s class='ur' />"%(site_email)
  print "<input name='pwd' value=%s class='pw' />"%(site_password)
  print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'kbt4' /></div>"
  print "</form>"


  print "<form method='post' action='kbt5.py' style='display:none;'>"
  print "<input name='username' value=%s class='ur' />"%(site_email)
  print "<input name='pwd' value=%s class='pw' />"%(site_password)
  print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'kbt5' /></div>"
  print "</form>"






  print "<script src='../DataTableExtend.js'></script>"
  print "<script src='../layui/layui.js ''></script>"
  print "<script src='../jquery-3.2.1.js'></script>"
  print "<script src='../js/gongshi1.js'></script>"
  print "</body>"
  print "</html>"


else:
	print "error"
