
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


  var tableIns =table.render({
    elem: '#demo'
    ,height: 600
    ,data : mydata 
    ,page: false
    ,limit:30
    ,cols: [[ //表头
      {field: 'businesscode', title: '项目编码', totalRowText: '合计'}
      ,{field: 'businessname', title: '项目名称'}
      ,{field: 'businessman', title: '项目工时填报人员'}
      ,{field: 'Monday', title: thismonday,width:"9%"} 
      ,{field: 'Tuesday', title: thistuesday,width:"9%"}
      ,{field: 'Wednesday', title: thiswednesday,width:"9%"}
      ,{field: 'Thursday', title: thisthursday,width:"9%"}
      ,{field: 'Friday', title: thisfriday,width:"9%"}
      ,{field: 'ratio', title: '该项目总共累计挂靠工时/该项目计划工时',width:"18%"}
      ,{field: 'Judge', title: '审批状态'}
      ,{fixed: 'right', width:178, align:'center', toolbar: '#barDemo',width:"8%"}
    ]]
    ,done: function (res, curr, count) {// 表格渲染完成之后的回调
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
    if(obj.event === 'del'){ 
      layer.confirm('拒绝此工时提交', function(index){
      //obj.del();这里是操作
      var req = new XMLHttpRequest();
      req.open("GET","./rejectmydata.py?businesscode="+data.businesscode+"&businessman="+data.businessman+"&username="+username+"&mondaytime="+mondaytime,false);
      req.send(null);
      res = req.responseText;
      layer.close(index);
      location.reload();
      }) 
    };
    if(obj.event === 'edit'){ 
      layer.confirm('同意此工时提交', function(index){
      var req = new XMLHttpRequest();
      req.open("GET","./agreemydata1.py?businesscode="+data.businesscode+"&businessman="+data.businessman+"&username="+username+"&mondaytime="+mondaytime,false);
      req.send(null);
      res = req.responseText;
      res = res.replace(/\\\\/g,"\\")
      myjson = eval('(' + res + ')');
      
      var nonedone = myjson[0].nonedone
      
      var workertime = myjson[0].worktime
      var starttime = myjson[0].starttime
      var endtime = myjson[0].endtime
      var should = myjson[0].should
      var status = myjson[0].status
      console.log(myjson[0].starttime)
      var total = parseInt(obj.data.Monday) + parseInt(obj.data.Tuesday) + parseInt(obj.data.Wednesday) + parseInt(obj.data.Thursday) + parseInt(obj.data.Friday) 
      req.open("GET","./agreemydata.py?businesscode="+data.businesscode+"&businessman="+data.businessman+"&username="+username+"&mondaytime="+mondaytime+"&total="+total+"&businessname="+obj.data.businessname+"&nonedone="+nonedone+"&workertime="+workertime+"&starttime="+starttime+"&endtime="+endtime+"&should="+should+"&status="+status,false);
      req.send(null);
      res = req.responseText;
      console.log(res)
      layer.close(index);
      location.reload();
      }) 
    };
  }) 
  $('#all').click(function () {
    examineddata = 
    table.reload(
      "demo", {    elem: '#demo'
      ,height: 600
      ,data : mydata 
      ,page: false
      ,limit:30
      ,cols: [[ //表头
      {field: 'businesscode', title: '项目编码', totalRowText: '合计'}
      ,{field: 'businessname', title: '项目名称'}
      ,{field: 'businessman', title: '项目工时填报人员'}
      
      ,{field: 'Monday', title: thismonday,width:"9%"} 
      ,{field: 'Tuesday', title: thistuesday,width:"9%"}
      ,{field: 'Wednesday', title: thiswednesday,width:"9%"}
      ,{field: 'Thursday', title: thisthursday,width:"9%"}
      ,{field: 'Friday', title: thisfriday,width:"9%"}
      ,{field: 'ratio', title: '该项目总共累计挂靠工时/该项目计划工时',width:"18%"}
      ,{field: 'Judge', title: '审批状态'}
      ,{fixed: 'right', width:178, align:'center', toolbar: '#barDemo',width:"8%"}
      ]]
      })
  });
  $('#examined').click(function () {
    document.getElementById("unexamined").click();
    table.reload(
      "demo", {    elem: '#demo'
      ,height: 600
      ,data : examineddata
      ,page: false
      ,limit:30
      ,cols: [[ //表头
      {field: 'businesscode', title: '项目编码', totalRowText: '合计'}
      ,{field: 'businessname', title: '项目名称'}
      ,{field: 'businessman', title: '项目工时填报人员'}

      ,{field: 'Monday', title: thismonday,width:"9%"} 
      ,{field: 'Tuesday', title: thistuesday,width:"9%"}
      ,{field: 'Wednesday', title: thiswednesday,width:"9%"}
      ,{field: 'Thursday', title: thisthursday,width:"9%"}
      ,{field: 'Friday', title: thisfriday,width:"9%"}
      ,{field: 'ratio', title: '该项目总共累计挂靠工时/该项目计划工时',width:"18%"}
      ,{field: 'Judge', title: '审批状态'}
      ,{fixed: 'right', width:178, align:'center', toolbar: '#barDemo',width:"8%"}
      ]]
      }
    )
  })
  $('#unexamined').click(function () {
    table.reload(
      "demo", {    elem: '#demo'
      ,height: 600
      ,data : unexamineddata
      ,page: false
      ,limit:30
      ,cols: [[ //表头
      {field: 'businesscode', title: '项目编码', totalRowText: '合计'}
      ,{field: 'businessname', title: '项目名称'}
      ,{field: 'businessman', title: '项目工时填报人员'}
      ,{field: 'Monday', title: thismonday,width:"9%"} 
      ,{field: 'Tuesday', title: thistuesday,width:"9%"}
      ,{field: 'Wednesday', title: thiswednesday,width:"9%"}
      ,{field: 'Thursday', title: thisthursday,width:"9%"}
      ,{field: 'Friday', title: thisfriday,width:"9%"}
      ,{field: 'ratio', title: '该项目总共累计挂靠工时/该项目计划工时',width:"18%"}
      ,{field: 'Judge', title: '审批状态'}
      ,{fixed: 'right', width:178, align:'center', toolbar: '#barDemo',width:"8%"}
      ]]
      })
  });
});
   


