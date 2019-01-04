#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import cgi, cgitb 
import sqlite3 
form = cgi.FieldStorage() 
# 获取数据
site_name = form.getvalue('username')
site_url  = form.getvalue('pwd')


print "Content-type:text/html"
print

if site_name == "admin" and site_url == "cobot#2018":
	print "<!DOCTYPE html>"
	print "<html>"
	print "<head>"
	print "<meta charset='utf-8'>"
	print "<title>Hello</title>"
	print "</head>"
	print "<body>"
	print "<div>"
	print "<form method='post' action='admin1.py' style='display:none;'>"
	print "<input name='username' value=%s >"%(site_name)
	print "<input name='pwd' type='password' value=%s  >"%(site_url)
	print "<input type='submit' value='点这里登录' name = 'submit' id='middle' >"
	print "</form>"
	print "</div>"
	print "</body>"
	print "<script src='../js/middle.js'></script>"
	print "<script src='../layui/layui.js ''></script>"
	print "<script src='../jquery-3.2.1.js'></script>"
	print "</html>"
else:
	print "<!DOCTYPE html>"
	print "<html>"
	print "<head>"
	print "<meta charset='utf-8'>"
	print "<title>Hello</title>"
	print "</head>"
	print "<body>"
	print "<div>"
	print "<form method='post' action='kbt1.py' style='display:none;'>"
	print "<input name='username' value=%s >"%(site_name)
	print "<input name='pwd' type='password' value=%s  >"%(site_url)
	print "<input type='submit' value='点这里登录' name = 'submit' id='middle' >"
	print "</form>"
	print "</div>"
	print "</body>"
	print "<script src='../js/middle.js'></script>"
	print "<script src='../layui/layui.js ''></script>"
	print "<script src='../jquery-3.2.1.js'></script>"
	print "</html>"
