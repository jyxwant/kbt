//JavaScript代码区域
layui.use('element', function(){
  var element = layui.element;
  
});
$(window).resize(function () {
location.reload();
})

layui.use('form', function(){
  var form = layui.form;
  
  //监听提交
  form.on('submit(formDemo)', function(data){
    //layer.msg(JSON.stringify(data.field));
    return false;
  });
});
var mydata //= [{"emailname":"xiaoli@163.com","password":"xiaoli123","Name":"小李","Tuesday":"激活"},{"emailname":"xiaozhang@163.com","password":"xiaozhang123","Name":"小张","Tuesday":"未激活"},{"emailname":"xiaowang@163.com","password":"xiaowang123","Name":"小王","Tuesday":"未激活"},{"emailname":"xiaojiang@163.com","password":"xiaojiang123","Name":"小蒋","Tuesday":"激活"},{"emailname":"xiaowu@163.com","password":"xiaowu","Name":"小吴","Tuesday":"未激活"},];

function checkEmail(){
　　var myforms=document.forms;
　　var myemail=myforms[0].email.value;
　　var myReg=/^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+\.)+(com|cn|net|org)$/;
 
　　if(myReg.test(myemail)){
　　　　return true;
　　}else{
　　　　alert("邮箱格式不对!");
　　　　return false;
}
}

function business(){

	document.getElementById("business").click();
}

function change(){
	var theemail = document.getElementById('emailname').innerText
	console.log(theemail)
	var thepassword  = document.getElementById('password').value
	console.log(thepassword)
	var thename = document.getElementById('Name').value
	console.log(thename)
	var req = new XMLHttpRequest();
 	req.open("GET","./adminchange10.py?email="+theemail+"&password="+thepassword+"&name="+thename,false);
        req.send(null);
        res = req.responseText;
	console.log(res)
	res = res.replace(/\\\\/g,"\\")
	var json = eval('(' + res + ')');
	
	var oldname = json[0].name
	console.log(oldname)
        req.open("GET","./adminchange1.py?email="+theemail+"&password="+thepassword+"&name="+thename+"&oldname="+oldname,false);
        req.send(null);
        res = req.responseText;
	console.log(res)
	location.reload();

}

function addworker(){
	var theemail = document.getElementById('newemailname').value
	console.log(theemail)
	var thepassword  = document.getElementById('newpassword').value
	console.log(thepassword)
	var thename = document.getElementById('newname').value
	console.log(thename)
	　　var myforms=document.forms;
　　var myemail=theemail;
　　var myReg=/^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+\.)+(com|cn|net|org)$/;
 
　　if(myReg.test(myemail)){
	var req = new XMLHttpRequest();
        req.open("GET","./adminchange2.py?email="+theemail+"&password="+thepassword+"&name="+thename,false);
        req.send(null);
        res = req.responseText;
	console.log(res)
	location.reload();
　　　　return true;
　　}else{
　　　　alert("邮箱格式不对!");
    location.reload();
　　　　return false;
}
	



}

window.onload=function (){//页面加载时根据本周的起始时间传入数据
        var req = new XMLHttpRequest();
        req.open("GET","./admingetmydata1.py",false);
        req.send(null);
        res = req.responseText;
	res = res.replace(/\\\\/g,"\\")
	var json = eval('(' + res + ')');
	mydata = json
}


layui.use(['jquery', 'table', 'form','layer'], function(){
  var table = layui.table;
var $ = layui.jquery;
        var layer = layui.layer;
        var form = layui.form;

  layui.$.support.cors = true; //允许ajax跨域
  //第一个实例
form.on('select(testSelect)', function (data) {
            debugger;
            var elem = $(data.elem);
            var trElem = elem.parents('tr');
            var tableData = table.cache['grid'];
            // 更新到表格的缓存数据中，才能在获得选中行等等其他的方法中得到更新之后的值
            tableData[trElem.data('index')][elem.attr('name')] = data.value;
            // 其他的操作看需求 TODO
        });
 var _window = $(window).height();
myheight = _window - 350
  layui.$.support.cors = true; //允许ajax跨域
   var tableIns =table.render({
    elem: '#demo'
    ,height: myheight
    ,data : mydata 
    ,page: false
    ,limit:30
,toolbar: true //开启工具栏，此处显示默认图标，可以自定义模板，详见文档

    ,cols: [[ //表头

    {field: 'emailname', title: '用户名\n（邮箱）'}
      ,{field: 'password', title: '登录密码'}
      ,{field: 'Name', title: '姓名', totalRow: true,templet: '#Name'} 
      ,{fixed: 'right', width: 165, align:'center', toolbar: '#barDemo'}

    ]]
      ,done: function (res, curr, count) {// 表格渲染完成之后的回调
        
            $('div[lay-event="LAYTABLE_COLS"]').remove()
            $('div[lay-event="LAYTABLE_PRINT"]').remove()
          
    }
     
});
  table.on('tool(test)',function(obj)  {

    var index = layui.layer.open({
        title : "编辑用户",
        type : 1,
        content : 
         '<div class="layui-row" id="test1">'
+ '<div class="layui-col-md11">'
+ '<form class="layui-form" id="addEmployeeForm">'
+'<div class="layui-form-item">'
+                       ' <label class="layui-form-label">用户名 &nbsp;&nbsp;  （邮箱）：</label>'
+			'<label class="layui-form-label" id = "emailname">'+obj.data.emailname+'</label>'                      
+                 '</div>'
+'     <div class="layui-form-item">'
+                        '<label class="layui-form-label">用户姓名：</label>'
+	' <div class="layui-input-block">'
+                        '   <input type="text" id="Name" class="layui-input" value="'+obj.data.Name+'">'
+                      '</div>'

+                    '</div>'
+'<div class="layui-form-item">'
+                        '<label class="layui-form-label">用户密码：</label>'
+                        '<div class="layui-input-block">'
+                           ' <input type="text" id="password" class="layui-input" value="'+obj.data.password+'">'
+                       ' </div>'
+                   ' </div>'

+                '<div class="layui-form-item">'
+                   '<div class="layui-input-block">'
+                      '<button id = "editchild" class="layui-btn layui-btn-submit " onclick="change()"   lay-submit="" lay-filter="childsubmit">修改</button>'
+                    ' <button type="reset" class="layui-btn layui-btn-primary">重置</button>'
+               '</div>'
+           '</div>'
+      '</form>'
+   '</div>'
+'</div>'
        ,//弹出层页面
        area: ['500px', '300px']
    })
    form.on('submit(childsubmit)', function() {
      var newemailname = $('#emailname').val()
      var newpassword = $('#password').val()
      var newname = $('#Name').val()
             obj.update({
                    emailname:newemailname,
                    password:newpassword,
                    Name:newname
                });
        layer.close(index);
        return false
  }) 
        

    

    }) 

 $('#addRow').click(function () {
  var index = layer.open({
                        type:1,
                        title:"添加用户",
                        skin:"myclass",
                        area:["50%"],
                        content:
'<div class="layui-row" id="test" >'
+'           <div class="layui-col-md11">'
+'                <form class="layui-form" id="addEmployeeForm">'
+'                    <div class="layui-form-item">'
+'                        <label class="layui-form-label">用户名      &nbsp;&nbsp;（邮箱）：</label>'
+'                        <div class="layui-input-block">'
+'                            <input type="text" id="newemailname" class="layui-input">'
+'                        </div>'
+'                    </div>'
+'<div class="layui-form-item">'
+'                        <label class="layui-form-label">用户密码：</label>'
+'                        <div class="layui-input-block">'
+'                            <input type="text" id="newpassword" class="layui-input">'
+'                        </div>'
+'                    </div>'
+'<div class="layui-form-item">'
+'                        <label class="layui-form-label">用户姓名：</label>'
+'                        <div class="layui-input-block">'
+'                            <input type="text" id="newname" class="layui-input">'
+'                        </div>'
+'                    </div>'
+'                    <div class="layui-form-item">'
+'                        <div class="layui-input-block">'
+'                            <button class="layui-btn layui-btn-submit " onclick = "addworker()" lay-submit="" lay-filter="addsubmit">添加</button>'
+'<button type="reset" class="layui-btn layui-btn-primary">重置</button>'
+'                        </div>'
+'                    </div>'
+'                </form>'
+'            </div>'
+'        </div>'
                    });
form.on('submit(addsubmit)', function() {
      var newemailname = $('#newemailname').val()
      var newpassword = $('#newpassword').val()
      var newname = $('#newname').val()
      layer.close(index);
var tableObj = tableIns;
            var config = tableObj.config;
           var dataBak = [];   //定义一个空数组,用来存储之前编辑过的数据已经存放新数据
 var _window = $(window).height();
myheight = _window - 350
  layui.$.support.cors = true; //允许ajax跨域

table.reload("demo", {
                
    elem: '#demo'
    ,height: myheight
    ,data : dataBak 
    ,page: false
    ,cols: [[ //表头
     {field: 'emailname', title: '用户名\n&nbsp;（邮箱）'}
      ,{field: 'password', title: '登录密码'}
      ,{field: 'Name', title: '用户姓名'} 
    ]]
  })
form.render();
      return false
  }) 

        });
 


 $('#editchild').click(function () {
  alert("hello")
 
})
});
   
