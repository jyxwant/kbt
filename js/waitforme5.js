$(window).resize(function () {
location.reload();
})


function agree(){
var req = new XMLHttpRequest();
agreeremark = document.getElementById('agreeremark').value
req.open("GET","./agreemydata.py?businesscode="+agreedata.businesscode+"&businessman="+agreedata.businessman+"&username="+username+"&mondaytime="+mondaytime+"&total="+total+"&businessname="+agreedata.businessname+"&nonedone="+nonedone+"&workertime="+workertime+"&starttime="+starttime+"&endtime="+endtime+"&should="+should+"&status="+status+"&remark="+agreeremark,false);
      req.send(null);
      
      location.reload();

}
function reject(){
var req = new XMLHttpRequest();
rejectremark = document.getElementById('rejectremark').value
      req.open("GET","./rejectmydata.py?businesscode="+rejectdata.businesscode+"&businessman="+rejectdata.businessman+"&username="+username+"&mondaytime="+mondaytime+"&businessname="+rejectdata.businessname+"&remark="+rejectremark,false);
      req.send(null);
	location.reload();
}
var mydata //= [{"businesscode":"CGFras","businessname":"xx","ratio":"100/200","businessman":"Zhangsan","Monday":2,"Tuesday":4,"Wednesday":6,"Thursday":8,"Friday":8,"Judge":"审批通过"},{"businesscode":"C1","businessname":"xx","ratio":"100/200","businessman":"Zhangsan","Monday":2,"Tuesday":4,"Wednesday":6,"Thursday":8,"Friday":8,"Judge":"审批拒绝"},{"businesscode":"C2","businessname":"xx","ratio":"50/100","businessman":"Zhangsan","Monday":2,"Tuesday":4,"Wednesday":6,"Thursday":8,"Friday":8,"Judge":"审批通过"},{"businesscode":"C3","businessname":"xx","ratio":"60/200","businessman":"Zhangsan","Monday":2,"Tuesday":4,"Wednesday":6,"Thursday":8,"Friday":8,"Judge":"未审批"},{"businesscode":"C4","businessname":"xx","ratio":"100/200","businessman":"Zhangsan","Monday":2,"Tuesday":4,"Wednesday":6,"Thursday":8,"Friday":8,"Judge":"未审批"}];

var mydata
var start = document.getElementById('getstart').innerText
var end   = document.getElementById('getend').innerText
var username = document.getElementById('username').innerText
var mondaytime = document.getElementById('mondaytime').innerText
window.onload=function (){//页面加载时根据本周的起始时间传入数据
        var req = new XMLHttpRequest();
        req.open("GET","./getmydata1.py?start="+start+"&end="+end+"&username="+username+"&mondaytime="+mondaytime,false);
        req.send(null);
        res = req.responseText;
	res = res.replace(/\\\\/g,"\\")
	var json = eval('(' + res + ')');
	mydata = json
}
function kbt(){
	document.getElementById("kbt").click();
}
function changepassword(){
	  document.getElementById("changepwd").click();
}
thismonday = '周一('+ document.getElementById('monday').innerText+')'
thistuesday = '周二(' + document.getElementById('tuesday').innerText + ')'
thiswednesday = '周三('+document.getElementById('wednesday').innerText+')'
thisthursday = '周四('+ document.getElementById('thursday').innerText+')'
thisfriday = '周五('+ document.getElementById('friday').innerText +')'


layui.use(['jquery', 'table', 'form','layer'], function(){
  var table = layui.table;
  var $ = layui.jquery;
  var layer = layui.layer;
  var form = layui.form;
  var index = layer.load(1);
   var _window = $(window).height();
	myheight = _window * 0.6
   ifreload = 1
  var tableIns =table.render({
    elem: '#demo'
    ,height: myheight
    ,data : mydata 
    ,page: false
    ,limit:30
    ,cols: [[ //表头
      {field: 'businesscode', title: '项目编码', totalRowText: '合计',width:"14%"}
      ,{field: 'businessname', title: '项目名称'}
      ,{field: 'businessman', title: '人员',width:"6%"}
      ,{field: 'Monday', title: thismonday,width:"6%"} 
      ,{field: 'Tuesday', title: thistuesday,width:"6%"}
      ,{field: 'Wednesday', title: thiswednesday,width:"6%"}
      ,{field: 'Thursday', title: thisthursday,width:"6%"}
      ,{field: 'Friday', title: thisfriday,width:"6%"}
      ,{field: 'ratio', title: '累计工时',width:"8%"}
      ,{field: 'Judge', title: '审批状态',width:"8%"}
      ,{fixed: 'right', width:178, align:'center', toolbar: '#barDemo',width:"12%"}
    ]]
    ,done: function (res, curr, count) {// 表格渲染完成之后的回调
        ifreload = 0
	layer.close(index);
        examineddata = mydata.filter(function (e) { return e.Judge != "未审批"; });
        unexamineddata = mydata.filter(function (e) { return e.Judge == "未审批"; });
        for (var i in res.data) {
          var item = res.data[i];
          if (item.Judge == "审批通过" || item.Judge == "审批拒绝") {// 这里是判断需要禁用的条件（如：状态为0的）
            $('tr[data-index=' + i + '] a[lay-event="edit"]').remove()
            $('tr[data-index=' + i + '] a[lay-event="del"]').remove()
          }
        }
        count || this.elem.next('.layui-table-view').find('.layui-table-header').css('overflow', 'auto');
        layui.each($('select'), function (index, item) {
          var elem = $(item);
          elem.val(elem.data('value')).parents('div.layui-table-cell').css('overflow', 'visible');
        });
        form.render(null, 'test1'); 
        $(".layui-table th").css("font-weight", "bold");// 设定表格标题字体加粗

        LayUIDataTable.SetJqueryObj($);// 第一步：设置jQuery对象

        //LayUIDataTable.HideField('num');// 隐藏列-单列模式
        //LayUIDataTable.HideField(['num','match_guest']);// 隐藏列-多列模式

        var currentRowDataList = LayUIDataTable.ParseDataTable(function (index, currentData, rowData) {})
        $.each(currentRowDataList, function (index, obj) {
          /*
           * 通过遍历表格集合，拿到每行数据对象obj，通过obj["列名"]["row"]可以拿到行对象，obj["列名"]["cell"]可以拿到单元格对象
           * */
          if (obj['Judge'] && (obj['Judge'].value == "审批通过" || obj['Judge'].value == "审批拒绝")) {
            obj['Judge']["row"].css("background-color", "#FAB000");// 对行（row）进行高亮显示
          }
            obj['ratio']["cell"].css("font-weight",1000);
        })
    }
  });
  setTimeout("if(ifreload==1){location.reload();}",2000)
  form.on('select(choseweek)', function(data){
	if(data.value == 0){
	document.getElementById("waitforme1").click();
	}
	if(data.value == 1){
	document.getElementById("waitforme2").click();
	}
	if(data.value == 2){
	document.getElementById("waitforme3").click();
	}
	if(data.value == 3){
	document.getElementById("waitforme4").click();
	}
	if(data.value == 4){
	document.getElementById("waitforme5").click();
	}
  })
  table.on('tool(test)',function(obj)  {
    var data = obj.data;
    if(obj.event === 'detail'){ 
      layer.confirm(data.remark, function(index){
        layer.close(index);
      });

    };
    if(obj.event === 'del'){ 
      var index = layui.layer.open({
        title : "拒绝此工时提交",
        type : 1,
        content : 
'<div class="layui-row" id="test1">'
+  '<div class="layui-form-item layui-form-text">'
+    '<label class="layui-form-label">请填写</label>'
+ '<form class="layui-form" id="addEmployeeForm">'
+    '<div class="layui-input-block layui-col-md10">'
+      '<textarea name="desc"  class="layui-textarea" id="rejectremark">'+'拒绝'+'</textarea>'
+    '</div>'
+                '<div class="layui-form-item">'
+                   '<div class="layui-input-block">'
+                      '<button id = "editchild" class="layui-btn layui-btn-submit "  onclick="reject()" lay-submit="" lay-filter="childsubmit">拒绝</button>'
+               '</div>'
+           '</div>'
+      '</form>'
+ ' </div>'
+ ' </div>'
        ,//弹出层页面
        area: ['800px', '300px']
    })
    form.on('submit(childsubmit)', function() {

	//changeremark()
        layer.close(index);
	
        return false
  }) 
      //obj.del();这里是操作
      rejectdata= data
      


    };
    if(obj.event === 'edit'){ 
	var index = layui.layer.open({
        title : "同意此工时提交",
        type : 1,
        content : 
'<div class="layui-row" id="test1">'
+  '<div class="layui-form-item layui-form-text">'
+    '<label class="layui-form-label">请填写</label>'
+ '<form class="layui-form" id="addEmployeeForm">'
+    '<div class="layui-input-block layui-col-md10">'
+      '<textarea name="desc"  class="layui-textarea" id="agreeremark">'+'同意'+'</textarea>'
+    '</div>'
+                '<div class="layui-form-item">'
+                   '<div class="layui-input-block">'
+                      '<button id = "editchild" class="layui-btn layui-btn-submit "  onclick="agree()" lay-submit="" lay-filter="childsubmit">同意</button>'
+               '</div>'
+           '</div>'
+      '</form>'
+ ' </div>'
+ ' </div>'
        ,//弹出层页面
        area: ['800px', '300px']
    })
    form.on('submit(childsubmit)', function() {

	//changeremark()
        layer.close(index);
	
        return false
  }) 
      
      var req = new XMLHttpRequest();
      req.open("GET","./agreemydata1.py?businesscode="+data.businesscode+"&businessman="+data.businessman+"&username="+username+"&mondaytime="+mondaytime,false);
      req.send(null);
      res = req.responseText;
      res = res.replace(/\\\\/g,"\\")
      myjson = eval('(' + res + ')');
      agreedata = data
      nonedone = myjson[0].nonedone
      
      workertime = myjson[0].worktime
      starttime = myjson[0].starttime
      endtime = myjson[0].endtime
      should = myjson[0].should
      status = myjson[0].status
      console.log(myjson[0].starttime)
      total = parseInt(obj.data.Monday) + parseInt(obj.data.Tuesday) + parseInt(obj.data.Wednesday) + parseInt(obj.data.Thursday) + parseInt(obj.data.Friday) 
      
      
    };
  }) 

 $('#newcsv').click(function () {


var req = new XMLHttpRequest();
        req.open("GET","./waitcsv.py?businessmanager="+username,false);
        req.send(null);
        res = req.responseText;
	res = res.replace(/\\\\/g,"\\")
	var newcsv = eval('(' + res + ')');
      var jsonData = newcsv
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
      link.download =  "我管理的项目的项目人员.csv";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);


});

  $('#all').click(function () {
     var _window = $(window).height();
	myheight = _window - 350
    table.reload(
      "demo", {    elem: '#demo'
      ,height: myheight
      ,data : mydata 
      ,page: false
      ,limit:30
      ,cols: [[ //表头
      {field: 'businesscode', title: '项目编码', totalRowText: '合计',width:"14%"}
      ,{field: 'businessname', title: '项目名称'}
      ,{field: 'businessman', title: '人员',width:"6%"}
      
      ,{field: 'Monday', title: thismonday,width:"6%"} 
      ,{field: 'Tuesday', title: thistuesday,width:"6%"}
      ,{field: 'Wednesday', title: thiswednesday,width:"6%"}
      ,{field: 'Thursday', title: thisthursday,width:"6%"}
      ,{field: 'Friday', title: thisfriday,width:"6%"}
      ,{field: 'ratio', title: '累计工时',width:"8%"}
      ,{field: 'Judge', title: '审批状态',width:"8%"}
      ,{fixed: 'right', width:178, align:'center', toolbar: '#barDemo',width:"12%"}
      ]]
      })
  });
  $('#examined').click(function () {
    document.getElementById("unexamined").click();
 var _window = $(window).height();
	myheight = _window - 350
    table.reload(
      "demo", {    elem: '#demo'
      ,height: myheight
      ,data : examineddata
      ,page: false
      ,limit:30
      ,cols: [[ //表头
      {field: 'businesscode', title: '项目编码', totalRowText: '合计',width:"14%"}
      ,{field: 'businessname', title: '项目名称'}
      ,{field: 'businessman', title: '人员',width:"6%"}

      ,{field: 'Monday', title: thismonday,width:"6%"} 
      ,{field: 'Tuesday', title: thistuesday,width:"6%"}
      ,{field: 'Wednesday', title: thiswednesday,width:"6%"}
      ,{field: 'Thursday', title: thisthursday,width:"6%"}
      ,{field: 'Friday', title: thisfriday,width:"6%"}
      ,{field: 'ratio', title: '累计工时',width:"8%"}
      ,{field: 'Judge', title: '审批状态',width:"8%"}
      ,{fixed: 'right', width:178, align:'center', toolbar: '#barDemo',width:"12%"}
      ]]
      }
    )
  })
  $('#unexamined').click(function () {
	 var _window = $(window).height();
	myheight = _window - 350
    table.reload(
      "demo", {    elem: '#demo'
      ,height: myheight
      ,data : unexamineddata
      ,page: false
      ,limit:30
      ,cols: [[ //表头
      {field: 'businesscode', title: '项目编码', totalRowText: '合计',width:"14%"}
      ,{field: 'businessname', title: '项目名称'}
      ,{field: 'businessman', title: '人员',width:"6%"}
      ,{field: 'Monday', title: thismonday,width:"6%"} 
      ,{field: 'Tuesday', title: thistuesday,width:"6%"}
      ,{field: 'Wednesday', title: thiswednesday,width:"6%"}
      ,{field: 'Thursday', title: thisthursday,width:"6%"}
      ,{field: 'Friday', title: thisfriday,width:"6%"}
      ,{field: 'ratio', title: '累计工时',width:"8%"}
      ,{field: 'Judge', title: '审批状态',width:"8%"}
      ,{fixed: 'right', width:178, align:'center', toolbar: '#barDemo',width:"12%"}
      ]]
      })
  });
});
   


