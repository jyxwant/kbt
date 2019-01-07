#!/usr/bin/python2
# -*- coding: UTF-8 -*-
import cgi, cgitb 
import sqlite3 

form = cgi.FieldStorage() 
# 获取数据
site_email = form.getvalue('username')
site_password  = form.getvalue('pwd')
thisname = form.getvalue('thisname')



print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部
print "<!DOCTYPE html>"
print "<html>"
print "<head>"
print "  <meta charset='utf-8'>"
print "  <meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1'>"
print "  <title>项目工时管理系统</title>"
print "  <link rel='stylesheet' href='../layui/css/layui.css'>"
print "</head>"
print "<body class='layui-layout-body'>"
print "<form method='post' action='waitforme1.py' style='display:none;'>"
print "<input name='username' value=%s class='ur' />"%(site_email)
print "<input name='pwd' value=%s class='pw' />"%(site_password)
print "<input name='thisname' value=%s class='pw' />"%(thisname)
print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'waitforme' /></div>"
print "</form>"
print "<body class='layui-layout-body'>"
print "<form method='post' action='kbt1.py' style='display:none;'>"
print "<input name='username' value=%s class='ur' />"%(site_email)
print "<input name='pwd' value=%s class='pw' />"%(site_password)
print "<input type='submit' value='点这里登录' name = 'submit' class='bn' id = 'kbt' /></div>"
print "</form>"

print "<div id='myname' style='display:none;'>%s</div>"%(site_email)
print "<div class='layui-layout layui-layout-admin'>"
print "  <div class='layui-header'>   "
print "   <!-- 头部区域（可配合layui已有的水平导航） -->"
print "    <ul class='layui-nav layui-layout-left'>"
print "      <li class='layui-nav-item '><a href='#' onclick = 'kbt()'>工时填写</a></li>"
print "      <li class='layui-nav-item'><a href='#' onclick = 'waitforme()'>待我审批的工时</a></li>"
print "      <li class='layui-nav-item layui-this'><a href='#' onclick='location.reload();'>修改密码</a></li> "
print "    </ul>"
print "    <ul class='layui-nav layui-layout-right'>"
print "      <li class='layui-nav-item'><a href='#'>%s</a></li><!--python-->"%(site_email)
print "    </ul>"
print "  </div>"
 
print "  <div class='layui-side layui-bg-black'>"
print "    <div class='layui-side-scroll'>"
print "      <!-- 左侧导航区域（可配合layui已有的垂直导航） -->"
print "      <ul class='layui-nav layui-nav-tree'  lay-filter='test'>"
print "        <li class='layui-nav-item layui-nav-itemed'>"
print "          <a class='' href='javascript:;'>修改密码</a>"
print "        </li>"

print "      </ul>"
print "    </div>"
print "  </div>"
  
print "  <div class='layui-body'>"
print "    <!-- 内容主体区域 -->"
print "    <div style='padding: 8px;'>"


print "<form class='layui-form' action=''>"
print "  <div class='layui-form-item'>"
print "    <label class='layui-form-label'>输入原密码</label>"
print "    <div class='layui-input-block'>"
print "      <input type='text' name='source' id='source' lay-verify='required' autocomplete='off' placeholder='请输入原密码' class='layui-input'>"
print "    </div>"
print "  </div>"
print "  <div class='layui-form-item'>"
print "    <label class='layui-form-label'>输入新密码</label>"
print "    <div class='layui-input-block'>"
print "      <input type='password' name='thenew' id='new' lay-verify='required' placeholder='请输入新密码' autocomplete='off' class='layui-input'>"
print "    </div>"
print "  </div>"
print "<div class='layui-form-item'>"
print "    <label class='layui-form-label'>确认新密码</label>"
print "    <div class='layui-input-block'>"
print "      <input type='password' name='renew' id='renew' lay-verify='required' placeholder='确认新密码' autocomplete='off' class='layui-input'>"
print "    </div>"
print "  </div>"
  
 
  
 
print "  <!--<div class='layui-form-item layui-form-text'>"
print "    <label class='layui-form-label'>编辑器</label>"
print "    <div class='layui-input-block'>"
print "      <textarea class='layui-textarea layui-hide' name='content' lay-verify='content' id='LAY_demo_editor'></textarea>"
print "    </div>"
print "  </div>-->"
print "  <div class='layui-form-item'>"
print "    <div class='layui-input-block'>"
print "      <button class='layui-btn' lay-submit='' lay-filter='demo1'>立即提交</button>"
print "    </div>"
print "  </div>"
print "</form>"

      
print "  </div>"


 
print "    </div>"

  
print "  <div class='layui-footer'>"
print "    <!-- 底部固定区域 -->"
print "    © 武汉库柏特科技有限公司-项目工时管理系统"
print "  </div>"
print "</div>"
print "<script src='../DataTableExtend.js'></script>"
print "<script src='../layui/layui.js '></script>"
print "<script src='../jquery-3.2.1.js'></script>"

print "<script src='../js/changepassword.js'></script>"


   



print "</body>"
print "</html>"
