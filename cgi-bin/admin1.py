#!/usr/bin/python2
# -*- coding: UTF-8 -*-
# CGI处理模块
import json
import cgi, cgitb 
import sqlite3 
import requests


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
	print "  <meta charset='utf-8'>"
	print "  <meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1'>"
	print "  <title>项目工时管理系统</title>"
	print "  <link rel='stylesheet' href='../layui/css/layui.css'>"
	print "  <link rel='stylesheet' href='../css/mycss.css'>"
	print "</head>"
	print "<body class='layui-layout-body' style='overflow-y:scroll;'>"
	print "<form method='post' action='admin2.py' style='display:none;'>"
	print "<input name='username' value=%s >"%(site_name)
	print "<input name='pwd' type='password' value=%s  >"%(site_url)
	print "<input type='submit' value='点这里登录' name = 'submit' id='business' >"
	print "</form>"
	print "<div class='layui-layout layui-layout-admin'>"
	print "  <div class='layui-header'>   "
	print "   <!-- 头部区域（可配合layui已有的水平导航） -->"
	print "    <ul class='layui-nav'>"
	print "      <li class='layui-nav-item layui-this'><a href='#' onclick='location.reload();'>管理用户</a></li>"
	print "      <li class='layui-nav-item'><a href='#' onclick = 'business()'>管理项目</a></li>"
	print "    </ul>"
	print "    <ul class='layui-nav layui-layout-right'>"
	print "      <li class='layui-nav-item'><a href=''>admin</a></li><!--python-->"
	print "    </ul>"
	print "  </div>  "
	print "  <div >"
	print "    <!-- 内容主体区域 -->"
	print "    <div style='padding: 8px;padding-top:0px;'>"
	print "<div class='layui-row' style='padding:0px;'>"
	print "    <div class='layui-col-md12' style='margin-bottom:40px'>"
	print "              <table class='layui-table'>"
	print "<table id='demo' lay-filter='test'></table>"

	print "<script type='text/html' id='toolbarDemo'>"
	print "  <div class='layui-btn-container'>"
	print "    <button class='layui-btn layui-btn-sm' lay-event='add'>添加</button>"
	print "    <button class='layui-btn layui-btn-sm' lay-event='delete'>删除</button>"
	print "    <button class='layui-btn layui-btn-sm' lay-event='update'>编辑</button>"
	print "  </div>"
	print "</script>"
	print "<script type='text/html' id='barDemo'>"
	print "  <a class='layui-btn layui-btn-xs' lay-event='edit'>编辑</a>"
  
	print "</script>"

      
	print "  </div>"
	print "</form>"


	print "<div class='layui-row'>"
	print "	<button class='layui-btn' id='addRow'>添加一个用户</button>"

	print "</div>"
	print "<p>说明<p>"
	print "<p>1.如果数据没有加载出来，请刷新一下</p>"
	print "<p>2.用户名（邮箱）是唯一的，不允许修改</p>"
	print "<p>3.要修改用户名（邮箱）需要到数据库修改</p>"
 
	print "    </div>"
	print "  </div>"
  
	print "  <div>"
	print "    <!-- 底部固定区域 -->"
	print "    © 武汉库柏特科技有限公司-项目工时管理系统"
	print "  </div>"
	print "</div>"
	print "<script src='../DataTableExtend.js'></script>"
	print "<script src='../layui/layui.js '></script>"
	print "<script src='../jquery-3.2.1.js'></script>"


	print "<script src ='../js/newadmin5.js'></script>"
	print "</body>"
	print "</html>"

