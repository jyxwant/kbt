#!/usr/bin/python2
# -*- coding: UTF-8 -*-
import cgi, cgitb 
import sqlite3 
import datetime
from datetime import timedelta
form = cgi.FieldStorage() 
# 获取数据
site_email = form.getvalue('username')
site_password  = form.getvalue('pwd')
thisname = form.getvalue('thisname')


now = datetime.datetime.now()
monday = now - timedelta(days=now.weekday()+14)
getstart = str(monday.year) + '-' + str(monday.month).zfill(2) + '-' + str(monday.day).zfill(2)
mondaytime = str(monday.year) + '-' + str(monday.month).zfill(2) + '-' + str(monday.day).zfill(2)
monday =  str(monday.month).zfill(2) + '/' + str(monday.day).zfill(2)

tuesday = now - timedelta(days=(now.weekday() + 13))
tuesday =  str(tuesday.month).zfill(2) + '/' + str(tuesday.day).zfill(2)
wednesday = now - timedelta(days=now.weekday() + 12)
wednesday =  str(wednesday.month).zfill(2) + '/' + str(wednesday.day).zfill(2)
thursday = now - timedelta(days=now.weekday() + 11)
thursday =  str(thursday.month).zfill(2) + '/' + str(thursday.day).zfill(2)
friday = now - timedelta(days=now.weekday() + 10)
getend = str(friday.year) + '-' + str(friday.month).zfill(2) + '-' + str(friday.day).zfill(2)
friday =  str(friday.month).zfill(2) + '/' + str(friday.day).zfill(2)
last_zero_monday =  now - timedelta(days=now.weekday())
last_zero_friday = now - timedelta(days=(now.weekday() - 4))
last_zero = '本周' + '(' + str(last_zero_monday.month).zfill(2) + '/' + str(last_zero_monday.day).zfill(2) + '-' +  \
str(last_zero_friday.month).zfill(2) + '/' + str(last_zero_friday.day).zfill(2) + ')'
last_one_monday = now - timedelta(days=(now.weekday() + 7))
last_one_friday = now - timedelta(days=(now.weekday() + 3))
last_one = '上一周' + '('+ str(last_one_monday.month).zfill(2) + '/' + str(last_one_monday.day).zfill(2) + '-' + \
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
last_four = '上四周' + '(' + str(last_four_monday.month).zfill(2) + '/' + str(last_four_monday.day).zfill(2) + '-' + \
str(last_four_friday.month).zfill(2) + '/' + str(last_four_friday.day).zfill(2) + ')'
thewait = "kbt2.py"
if now.weekday() >= 4:
  thewait = "kbt1.py"
print "Content-type:text/html"
print

print  "<!DOCTYPE html>"
print  "<html>"
print  "<head>"
print    "<meta charset='utf-8'>"
print    "<meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1'>"
print    "<title>项目工时管理系统</title>"
print    "<link rel='stylesheet' href='../layui/css/layui.css'>"
print "  <link rel='stylesheet' href='../css/mycss1.css'>"
print  "</head>"
print  "<body class='layui-layout-body'>"
print  "<div class='layui-layout layui-layout-admin'>"


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


print "</form>"
print "<body class='layui-layout-body' style='overflow-y:scroll;'>"
print "<form method='post' action='%s' style='display:none;'>"%(thewait)
print "<input name='username' value=%s class='ur' />"%(site_email)
print "<input name='pwd' value=%s class='pw' />"%(site_password)
print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'kbt' /></div>"
print "</form>"



print  "  <div class='layui-header'>   "
print  "   <!-- 头部区域（可配合layui已有的水平导航） -->"
print  "    <ul class='layui-nav '>"
print  "      <li class='layui-nav-item '><a href='#' onclick = 'kbt()'>工时填写</a></li>"
print  "      <li class='layui-nav-item layui-this'><a href='#' onclick='location.reload();'>待我审批的工时</a></li>"
print  "      <li class='layui-nav-item'><a href='#' onclick='changepassword()'>修改密码</a></li> "
print  "    </ul>"
print  "    <ul class='layui-nav layui-layout-right'>"
print "      <li class='layui-nav-item'><a href='#'>%s</a></li><!--python-->"%(site_email)
print  "    </ul>"
print  "  </div>"




  
print  "  <div>"
print  "    <!-- 内容主体区域 -->"
print  "    <div style='padding: 8px;padding-top:0px;'>"
print  "      <div class='layui-row' id='test' style='display: none;' height=100px>"
print  "        <div class='layui-col-md11'>"
print  "          <form class='layui-form' id='addEmployeeForm' lay-filter='test1'>"
              
print  "            <div class='layui-form-item'>"
print  "              <label class='layui-form-label'>项目编码：</label>"
print  "                <div class='layui-input-block'>"
print  "                  <select class='layui-input' name='deptId' id='deptSelect'>"
print  "                    <option value=''></option>"
print  "                    <option value='GPS'>GPS-导航系统-张三</option><!--python-->"
print  "                    <option value='DPS'>DPS-数字信号处理-李四</option><!--python-->"
print  "                  </select>"
print  "                </div>"
print  "            </div>"

print  "            <div class='layui-form-item'>"
print  "              <div class='layui-input-block'>"
print  "                <br/>"
print  "                <br/>"
print  "                <br/>"
print  "                <br/>"
print  "                <br/>"
print  "                <br/>"
print  "                <br/>"
print  "              </div>"
print  "            </div>"

print  "            <div class='layui-form-item'>"
print  "              <div class='layui-input-block'>"
print  "                <button type='button' class='layui-btn layui-btn-normal'>提交</button>"
print  "              </div>"
print  "            </div>"

print  "          </form>"
print  "        </div>"
print  "      </div>"
    
print  "      <div class='layui-row' style='padding: 0px;    padding-buttom:0px;'>"
      
print  "        <div class='layui-col-md5'>"
print  "          <form class='layui-form' action=''>"
          
print "            <select name='city'  lay-verify='' id='#selected' lay-filter='choseweek' >"
print "               <option value='' lay-filter='twoweek' >%s</option>"%(last_two)
print "              <option value='0' lay-filter='zeroweek' >%s</option>"%(last_zero)
print "                <option value='1' lay-filter='oneweek'>%s</option>"%(last_one)
print "               <option value='2' lay-filter='twoweek' selected>%s</option>"%(last_two)
print "                <option value='3' lay-filter='threeweek'>%s</option>"%(last_three)
print "                <option value='4' lay-filter='fourweek'>%s</option>"%(last_four)
print "            </select>"

print  "          </form>"
print  "        </div>"

print  "      <div class='layui-col-md7'>"
print  "      </div>"

print  "    </div>"


print  "    <div class='layui-row' style='padding:0px;'>"
print  "      <div class='layui-col-md12' style='margin-bottom:40px'>"

print  "<div style='text-align: center;'>"
print  "  <div>"


print  "        <table id='demo' lay-filter='test'></table>"
print  "  </div>"
print  "</div>"
print  "	<script type='text/html' id='barDemo'>"
print  "		<a class='layui-btn layui-btn-xs' lay-event='edit'>同意</a>"
print  "  		<a class='layui-btn layui-btn-danger layui-btn-xs' lay-event='del'>拒绝</a>"
print  "  		<a class='layui-btn layui-btn-primary layui-btn-xs' lay-event='detail'>查看工时说明</a>"
print  "	</script>"

print  "      </div>"

print  "      <div class='layui-row'>"
print  "        <button class='layui-btn' id='all'>查看全部工时</button>"
print  "        <button class='layui-btn' id='examined'>已审批的工时</button>"
print  "        <button class='layui-btn' id='unexamined'>未审批的工时</button>"
print  "        <button class='layui-btn' id='newcsv'>导出我的项目分析</button>"
print  "      </div>"
print  "      <p>审批说明<p>"
print  "      <p>1.审批拒绝的工时请填写拒绝的理由；</p>"
print  "	<p>2.如果数据没有加载出来，请尝试刷新页面<p>"
print  "    </div>"
print  "  </div>"
  
print  "  <div >"
print  "    <!-- 底部固定区域 -->"
print  "    © 武汉库柏特科技有限公司-项目工时管理系统"
print  "  </div>"
print  "</div>"

print "<form method='post' action='changepassword.py' style='display:none;'>"
print "<input name='username' value=%s class='ur' />"%(site_email)
print "<input name='pwd' value=%s class='pw' />"%(site_password)
print "<input name='thisname' value=%s class='pw' />"%(thisname)
print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'changepwd' /></div>"
print "</form>"

print "<form method='post' action='waitforme1.py' style='display:none;'>"
print "<input name='username' value=%s class='ur' />"%(site_email)
print "<input name='pwd' value=%s class='pw' />"%(site_password)
print "<input name='thisname' value=%s class='pw' />"%(thisname)
print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'waitforme1' /></div>"
print "</form>"

print "<form method='post' action='waitforme2.py' style='display:none;'>"
print "<input name='username' value=%s class='ur' />"%(site_email)
print "<input name='pwd' value=%s class='pw' />"%(site_password)
print "<input name='thisname' value=%s class='pw' />"%(thisname)
print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'waitforme2' /></div>"
print "</form>"

print "<form method='post' action='waitforme3.py' style='display:none;'>"
print "<input name='username' value=%s class='ur' />"%(site_email)
print "<input name='pwd' value=%s class='pw' />"%(site_password)
print "<input name='thisname' value=%s class='pw' />"%(thisname)
print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'waitforme3' /></div>"
print "</form>"

print "<form method='post' action='waitforme4.py' style='display:none;'>"
print "<input name='username' value=%s class='ur' />"%(site_email)
print "<input name='pwd' value=%s class='pw' />"%(site_password)
print "<input name='thisname' value=%s class='pw' />"%(thisname)
print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'waitforme4' /></div>"
print "</form>"

print "<form method='post' action='waitforme5.py' style='display:none;'>"
print "<input name='username' value=%s class='ur' />"%(site_email)
print "<input name='pwd' value=%s class='pw' />"%(site_password)
print "<input name='thisname' value=%s class='pw' />"%(thisname)
print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'waitforme5' /></div>"
print "</form>"


print  "<script src='../DataTableExtend.js'></script>"
print  "<script src='../layui/layui.js '></script>"
print  "<script src='../jquery-3.2.1.js'></script>"
print  "<script src='../js/waitforme4.js'></script>"
