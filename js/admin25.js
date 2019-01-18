//JavaScript代码区域
layui.use('element', function(){
  var element = layui.element;
  
});
$(window).resize(function () {
location.reload();
})


function managergongshi(){
        var req = new XMLHttpRequest();
        req.open("GET","./adminmanager.py",false);
        req.send(null);
        res = req.responseText;
	res = res.replace(/\\\\/g,"\\")
	console.log(res)
	var json = eval('(' + res + ')');
	var theworker = json
	let str = '项目经理,项目人员,项目编码,项目名称,时间\n'
  var strarray = new Array()
  for(let i = 0; i < theworker.length;i++ ){
	strarray[i] = ''
	
			strarray[i] += theworker[i].businessmanager + '\t,'
			strarray[i] += theworker[i].businessworker + '\t,'
strarray[i] += theworker[i].businesscode + '\t,'
strarray[i] += theworker[i].businessname + '\t,'
strarray[i] += theworker[i].mondaytime + '\t,'
			strarray[i] += '\n';
		
		

	}
  for(let i = 0; i < strarray.length;i++){
	str += strarray[i]
}
	      //encodeURIComponent解决中文乱码
      let uri = 'data:text/csv;charset=utf-8,\ufeff' + encodeURIComponent(str);
      //通过创建a标签实现
      var link = document.createElement("a");
      link.href = uri;
      //对下载的文件命名
      link.download =  "四周内未审批工时人员.csv";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

}
function workergongshi(){
        var req = new XMLHttpRequest();
        req.open("GET","./adminpeople.py",false);
        req.send(null);
        res = req.responseText;
	res = res.replace(/\\\\/g,"\\")
	console.log(res)
	var json = eval('(' + res + ')');
	var theworker = json
	let str = '姓名,时间\n'
  var strarray = new Array()
  for(let i = 0; i < theworker.length;i++ ){
	strarray[i] = ''
	
			strarray[i] += theworker[i].name + '\t,'
			strarray[i] += theworker[i].mondaytime + '\t,'
			strarray[i] += '\n';
		
		

	}
  for(let i = 0; i < strarray.length;i++){
	str += strarray[i]
}
	      //encodeURIComponent解决中文乱码
      let uri = 'data:text/csv;charset=utf-8,\ufeff' + encodeURIComponent(str);
      //通过创建a标签实现
      var link = document.createElement("a");
      link.href = uri;
      //对下载的文件命名
      link.download =  "四周内未提交工时人员.csv";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

}

function change(){

	var changebusinesscode = document.getElementById('changebusinesscode').innerText
	var changebusinessname  = document.getElementById('changebusinessname').value
	var obj = document.getElementById('changebusinessmanager'); //定位id
	var index = obj.selectedIndex; // 选中索引
	var changebusinessmanager = obj.options[index].text; // 选中文本
	var value = obj.options[index].value; // 选中值
	var sobj = document.getElementById('changestatus'); //定位id
	var sindex = sobj.selectedIndex; // 选中索引
	var changebusinessstatus = sobj.options[sindex].text; // 选中文本
	var svalue = sobj.options[sindex].value; // 选中值
	var changestartyear  = document.getElementById('changestartyear').value
	var changestartmonth  = document.getElementById('changestartmonth').value
	var changestartday  = document.getElementById('changestartday').value
	var changestart = changestartyear +'-'+ zfill(changestartmonth,2) +'-' +zfill(changestartday,2)
	var changeendyear  = document.getElementById('changeendyear').value
	var changeendmonth  = document.getElementById('changeendmonth').value
	var changeendday  = document.getElementById('changeendday').value
	var changeend = changeendyear +'-'+ zfill(changeendmonth,2) +'-' +zfill(changeendday,2)
	var changeshould  = document.getElementById('changeshould').value
	var hasdone = document.getElementById('hasdone').innerText
	var req = new XMLHttpRequest();
  req.open("GET","./adminedit.py?businesscode="+changebusinesscode+"&businessname="+changebusinessname+"&businessmanager="+changebusinessmanager+"&start="+changestart+"&end="+changeend+"&should="+changeshould + "&now="+hasdone+"&status="+changebusinessstatus,false);
  req.send(null);
  res = req.responseText;
  console.log(res)
	location.reload();
}

 function zfill(num, n) {
            return (Array(n).join(0) + num).slice(-n);
        }
function addbusiness(){
	var addbusinesscode = document.getElementById('addbusinesscode').value
	console.log(addbusinesscode)
	var addbusinessname  = document.getElementById('addbusinessname').value
	console.log(addbusinessname)
	var obj = document.getElementById('addbusinessmanager'); //定位id
	var index = obj.selectedIndex; // 选中索引
	var addbusinessmanager = obj.options[index].text; // 选中文本
	var value = obj.options[index].value; // 选中值
	console.log(addbusinessmanager)
	var addstartyear  = document.getElementById('addstartyear').value
	var addstartmonth  = document.getElementById('addstartmonth').value
	var addstartday  = document.getElementById('addstartday').value
	var addstart = addstartyear +'-'+ zfill(addstartmonth,2) +'-' +zfill(addstartday,2)
	console.log(addstart)
	var addendyear  = document.getElementById('addendyear').value
	var addendmonth  = document.getElementById('addendmonth').value
	var addendday  = document.getElementById('addendday').value
	var addend = addendyear +'-'+ zfill(addendmonth,2) +'-' +zfill(addendday,2)
	console.log(addend)
	var addshould  = document.getElementById('addshould').value
	console.log(addshould)
	var req = new XMLHttpRequest();
  req.open("GET","./adminadd.py?businesscode="+addbusinesscode+"&businessname="+addbusinessname+"&businessmanager="+addbusinessmanager+"&start="+addstart+"&end="+addend+"&should="+addshould,false);
  req.send(null);
  res = req.responseText;
  console.log(res)
	location.reload();
	

}

function workercsv(){
  let str = '用户名（邮箱）,姓名,挂靠项目,挂靠项目名称,累计挂靠时间\n'
  var strarray = new Array()
  for(let i = 0; i < allname.length;i++ ){
	strarray[i] = ''
	for(let j = 0; j < mydata.length;j++){
		if(mydata[j].businessworker == allname[i].name){
			strarray[i] += allname[i].email + '\t,'
			strarray[i] += allname[i].name + '\t,'
			strarray[i] += mydata[j].businesscode + '\t,'
			strarray[i] += mydata[j].businessname + '\t,'
			strarray[i] += mydata[j].workertime + '\t,'
			strarray[i] += '\n';
		}

	}		

	}
  for(let i = 0; i < strarray.length;i++){
	str += strarray[i]
}
	      //encodeURIComponent解决中文乱码
      let uri = 'data:text/csv;charset=utf-8,\ufeff' + encodeURIComponent(str);
      //通过创建a标签实现
      var link = document.createElement("a");
      link.href = uri;
      //对下载的文件命名
      link.download =  "按人员导出数据表.csv";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
}



function businesscsv(){

      var jsonData = mydata
      let str = '项目编码,项目名称,项目经理,项目状态,累计挂靠工时,项目工时挂靠人员,此员工累计挂靠时间,是否已经超标,项目开始时间,项目结束时间,设定的工时上限\n';
      //增加\t为了不让表格显示科学计数法或者其他格式
      for(let i = 0 ; i < jsonData.length ; i++ ){
     
            str+=jsonData[i].businesscode + '\t,';
str+=jsonData[i].businessname + '\t,';
str+=jsonData[i].businessmanager + '\t,';
str+=jsonData[i].status + '\t,';
str+=jsonData[i].now + '\t,';
str+=jsonData[i].businessworker + '\t,';
str+=jsonData[i].workertime + '\t,';
str+=jsonData[i].beyond + '\t,';
str+=jsonData[i].start + '\t,';
str+=jsonData[i].end + '\t,';
str+=jsonData[i].should + '\t';
	     

        str+='\n';
      }
      //encodeURIComponent解决中文乱码
      let uri = 'data:text/csv;charset=utf-8,\ufeff' + encodeURIComponent(str);
      //通过创建a标签实现
      var link = document.createElement("a");
      link.href = uri;
      //对下载的文件命名
      link.download =  "按项目导出数据表.csv";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);


}

function worker(){

	document.getElementById("worker").click();
}
var mydata //= [{"businessname":"gps","businessmanager":"导航系统","Monday":"小李","Tuesday":"激活","1":200,"2":"小李","3":50,"4":"是","5":"2019/1/1","6":"2019/1/29","7":300}];
var allname


window.onload=function (){//页面加载时根据本周的起始时间传入数据
        var req = new XMLHttpRequest();
        req.open("GET","./admingetmydata2.py",false);
        req.send(null);
        res = req.responseText;
	res = res.replace(/\\\\/g,"\\")
	var json = eval('(' + res + ')');
	mydata = json
	req.open("GET","./admingetmydata3.py",false);
        req.send(null);
        res = req.responseText;
	
	res = res.replace(/\\\\/g,"\\")
	res = eval('(' + res + ')');
	console.log(res)
	allname = res
	selectstr = ''
	for(let i = 0; i < allname.length;i++){
	selectstr += "<option value='"+allname[i].email+"'>"+allname[i].name+"</option>"
} 
}



layui.use(['jquery', 'table', 'form','layer'], function(){
  var table = layui.table;
var $ = layui.jquery;
        var layer = layui.layer;
        var form = layui.form;
	 var _window = $(window).height();
	myheight = _window * 0.6
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
    ifreload = 1
var index = layer.load(1);
   var tableIns =table.render({
    elem: '#demo'
    ,height: myheight
    ,data : mydata 
    ,page: false
    ,limit:30

    ,cols: [[ //表头

    {field: 'businesscode', title: '项目编码'}
      ,{field: 'businessname', title: '项目名称'}
      ,{field: 'businessmanager', title: '项目经理',templet: '#monday'} 
      ,{field: 'status', title: '项目状态'}
      
,{field: 'now', title: '累计挂靠工时'}
,{field: 'businessworker', title: '项目工时挂靠人员'}
,{field: 'workertime', title: '此员工累计挂靠时间'}
,{field: 'beyond', title: '是否已经超标'}
,{field: 'start', title: '项目开始时间'}
,{field: 'end', title: '项目结束时间'}
,{field: 'should', title: '设定的工时上限'}
,{fixed: 'right', width: 165, align:'center', toolbar: '#barDemo'}
    ]]
      ,done:function (res) {   //返回数据执行回调函数
			    	layer.close(index);    //返回数据关闭loading
			    	ifreload = 0;
			    }
     
});

setTimeout("if(ifreload==1){location.reload();}",2000)
  table.on('tool(test)',function(obj)  {
    var data = obj.data;
    console.log('hello')
    console.log(data.businessmanager)
    var index = layui.layer.open({
        title : "编辑项目",
        type : 1,
        content : 
         "<div class='layui-row' id='test1' >"
+            "<div class='layui-col-md11'>"
+               " <form class='layui-form' id='addEmployeeForm'>"
+"<div class='layui-form-item'>"
+ "<div id='changebusinesscode' style='display:none;'>"+data.businesscode +"</div>"
+ "<div id='hasdone' style='display:none;'>"+data.now +"</div>"
+                        "<label class='layui-form-label'>项目名称：</label>"
+                        "<div class='layui-input-block'>"
+                            "<input type='text' id='changebusinessname' class='layui-input' value='"+data.businessname+"'>"
+                       " </div>"
+                   " </div>"
+ "<div class='layui-form-item'>"
+              "<label class='layui-form-label'>项目经理：</label>"
+               " <div class='layui-input-block'>"
+                  "<select class='layui-input' id='changebusinessmanager' id='deptSelect'>"
+                   " <option value='origin'>"+data.businessmanager+"</option>"
+                    selectstr
+                  "</select>"
+                "</div>"
+            "</div>"
+"<div class='layui-form-item'>"
+                        "<label class='layui-form-label'>项目创建时间：</label>"
+			"<label class='layui-form-label'>年：</label>"
+                        "<div class='layui-col-md2'>"
+                            "<input type='text' id='changestartyear' class='layui-input' value='"+data.start[0]+data.start[1]+data.start[2]+data.start[3]+"'>"
+                        "</div>"
+			"<label class='layui-form-label'>月：</label>"
+                        "<div class='layui-col-md1'>"
+                            "<input type='text' id='changestartmonth' class='layui-input' value='"+data.start[5]+data.start[6]+"'>"
+                        "</div>"
+			"<label class='layui-form-label'>日：</label>"
+                        "<div class='layui-col-md1'>"
+                            "<input type='text' id='changestartday' class='layui-input' value='"+data.start[8]+data.start[9]+"'>"
+                        "</div>"
+                    "</div>"
+"<div class='layui-form-item'>"
+                        "<label class='layui-form-label'>项目结束时间：</label>"
+			"<label class='layui-form-label'>年：</label>"
+                        "<div class='layui-col-md2'>"
+                            "<input type='text' id='changeendyear' class='layui-input' value='"+data.end[0]+data.end[1]+data.end[2]+data.end[3]+"'>"
+                        "</div>"
+			"<label class='layui-form-label'>月：</label>"
+                        "<div class='layui-col-md1'>"
+                           " <input type='text' id='changeendmonth' class='layui-input' value='"+data.end[5]+data.end[6]+"'>"
+                        "</div>"
+			"<label class='layui-form-label'>日：</label>"
+                        "<div class='layui-col-md1'>"
+                            "<input type='text' id='changeendday' class='layui-input' value='"+data.end[8]+data.end[9]+"'>"
+                        "</div>"
+                    "</div>"
+"<div class='layui-form-item'>"
+                        "<label class='layui-form-label'>设定的工时上限：</label>"
+                        "<div class='layui-input-block'>"
+                            "<input type='text' id='changeshould' class='layui-input' value='"+data.should+"'>"
+                        "</div>"
+                    "</div>"
+"<div class='layui-form-item'>"
+                        "<label class='layui-form-label'>状态：</label>"
+                        "<div class='layui-input-block'>"
+                  "<select class='layui-input'  id='changestatus'>"
+                   " <option value='origin' selected>"+data.status+"</option>"
+                    " <option value='yes'>"+"激活"+"</option>"
+                    " <option value='no'>"+"未激活"+"</option>"
+                  "</select>"
+                        "</div>"
+                    "</div>"
+                    "<div class='layui-form-item'>"
+                        "<div class='layui-input-block'>"
+                            "<button id = 'editchild' class='layui-btn layui-btn-submit ' onclick='change()'   lay-submit='' lay-filter='childsubmit'>修改</button>"
+                        "</div>"
+                    "</div>"
+                "</form>"
+            "</div>"
+        "</div>"
        ,//弹出层页面
        area: ['1000px', '600px']
    })
form.render();
    form.on('submit(childsubmit)', function() {
        layer.close(index);
        return false
  })

    }) 
 $('#addRow').click(function () {
    var index = layui.layer.open({
        title : "添加项目",
        type : 1,
        content : 
         "<div class='layui-row' id='test' >"
+           " <div class='layui-col-md11'>"
+               " <form class='layui-form' id='addEmployeeForm'>"   
+                    "<div class='layui-form-item'>"
+                        "<label class='layui-form-label'>项目编码：</label>"
+                        "<div class='layui-input-block'>"
+                            "<input type='text' id='addbusinesscode' class='layui-input'>"
+                        "</div>"
+                    "</div>"
+"<div class='layui-form-item'>"
+                        "<label class='layui-form-label'>项目名称：</label>"
+                        "<div class='layui-input-block'>"
+                            "<input type='text' id='addbusinessname' class='layui-input'>"
+                        "</div>"
+                    "</div>"
+ "<div class='layui-form-item'>"
+              "<label class='layui-form-label'>项目经理：</label>"
+                "<div class='layui-input-block'>"
+                  "<select class='layui-input' id='addbusinessmanager' id='deptSelect'>"
+                    "<option value=''></option>"
+			selectstr
+                  "</select>"
+                "</div>"
+            "</div>"
+"<div class='layui-form-item'>"
+                        "<label class='layui-form-label'>项目创建时间：</label>"
+			"<label class='layui-form-label'>年：</label>"
+                        "<div class='layui-col-md2'>"
+                            "<input type='text' id='addstartyear' class='layui-input'>"
+                        "</div>"
+			"<label class='layui-form-label'>月：</label>"
+                        "<div class='layui-col-md1'>"
+                            "<input type='text' id='addstartmonth' class='layui-input'>"
+                        "</div>"
+			"<label class='layui-form-label'>日：</label>"
+                        "<div class='layui-col-md1'>"
+                            "<input type='text' id='addstartday' class='layui-input'>"
+                        "</div>"

+                    "</div>"
+"<div class='layui-form-item'>"
+                        "<label class='layui-form-label'>项目结束时间：</label>"
+			"<label class='layui-form-label'>年：</label>"
+                        "<div class='layui-col-md2'>"
+                            "<input type='text' id='addendyear' class='layui-input'>"
+                        "</div>"
+			"<label class='layui-form-label'>月：</label>"
+                        "<div class='layui-col-md1'>"
+                            "<input type='text' id='addendmonth' class='layui-input'>"
+                        "</div>"
+			"<label class='layui-form-label'>日：</label>"
+                        "<div class='layui-col-md1'>"
+                            "<input type='text' id='addendday' class='layui-input'>"
+                        "</div>"
+                    "</div>"
+"<div class='layui-form-item'>"
+                        "<label class='layui-form-label'>项目累计工时上限：</label>"
+                        "<div class='layui-input-block'>"
+                            "<input type='text' id='addshould' class='layui-input'>"
+                        "</div>"
+                    "</div>"

+                    "<div class='layui-form-item'>"
+                        "<div class='layui-input-block'>"
+                            "<button id = 'addchild' class='layui-btn layui-btn-submit ' lay-submit='' lay-filter='childsubmit' onclick='addbusiness()'>添加</button>"
+                        "</div>"
+                    "</div>"
+                "</form>"
+            "</div>"
+        "</div>"


        ,//弹出层页面
        area: ['1000px', '500px']
    })
     form.on('submit(childsubmit)', function() {
        layer.close(index);
        return false
  })

form.render();
        });

        });
   
