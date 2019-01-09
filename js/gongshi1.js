//JavaScript代码区域
$(window).resize(function () {
location.reload();
})
function wait(){
	document.getElementById("waitforme").click();
}
layui.use('element', function(){
  var element = layui.element;
  
});



layui.use('form', function(){
  var form = layui.form;
  
  //监听提交
  form.on('submit(formDemo)', function(data){
    layer.msg(JSON.stringify(data.field));
    return false;
  });
});
//var mydata = [{"businesscode":"CGFras","businessname":"xx","businessmanager":"Zhangsan","Monday":2,"Tuesday":4,"Wednesday":6,"Thursday":8,"Friday":8,"Judge":"审批通过"},{"businesscode":"C1","businessname":"xx","businessmanager":"Zhangsan","Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Judge":"未审批"},{"businesscode":"C2","businessname":"xx","businessmanager":"Zhangsan","Monday":2,"Tuesday":4,"Wednesday":6,"Thursday":8,"Friday":0,"Judge":"审批通过"},{"businesscode":"C3","businessname":"xx","businessmanager":"Zhangsan","Monday":2,"Tuesday":4,"Wednesday":6,"Thursday":8,"Friday":8,"Judge":"审批通过"},{"businesscode":"C4","businessname":"xx","businessmanager":"Zhangsan","Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Judge":"未审批"}];
var mydata
var start = document.getElementById('getstart').innerText
var end   = document.getElementById('getend').innerText
var username = document.getElementById('username').innerText
var mondaytime = document.getElementById('mondaytime').innerText


function commitmydata(){
	
	if($('div[class="layui-table-total"] td[data-key="1-0-4"]')[0].innerText > 8){
		layer.confirm('周一的项目总工时超过8小时', function(index){layer.close(index); })
		
	}
	else if ($('div[class="layui-table-total"] td[data-key="1-0-5"]')[0].innerText > 8){
		layer.confirm('周二的项目总工时超过8小时', function(index){layer.close(index); })
		
	}
else if ($('div[class="layui-table-total"] td[data-key="1-0-6"]')[0].innerText > 8){
		layer.confirm('周三的项目总工时超过8小时', function(index){layer.close(index); })
		
	}
else if ($('div[class="layui-table-total"] td[data-key="1-0-7"]')[0].innerText > 8){
		layer.confirm('周四的项目总工时超过8小时', function(index){layer.close(index); })
		
	}
else if ($('div[class="layui-table-total"] td[data-key="1-0-8"]')[0].innerText > 8){
		layer.confirm('周五的项目总工时超过8小时', function(index){layer.close(index); })
		
	}
else{
	for(let n=0;n < mydata.length;n++){
		
	
	}

	for(let i=0;i < mydata.length;i++){
		if(mydata[i].Judge == "未审批" ){
			var businesscode = mydata[i].businesscode
			var monday = mydata[i].Monday
			var tuesday = mydata[i].Tuesday
			var wednesday = mydata[i].Wednesday
			var thursday = mydata[i].Thursday
			var friday  = mydata[i].Friday
			var businessmanager = mydata[i].businessmanager
			var req = new XMLHttpRequest();
        req.open("GET","./gongshicommit.py?businesscode="+businesscode+"&mondaytime="+mondaytime
+"&username="+username+"&monday="+monday+"&tuesday="+tuesday+"&wednesday="+wednesday+"&thursday="+thursday+"&friday="+friday+"&businessmanager="+businessmanager,false);
        req.send(null);
        res = req.responseText;
	console.log(res)	
		}
	location.reload();
	}
	}


}
function addbusiness(){
	var obj = document.getElementById('selectbusiness'); //定位id
	var index = obj.selectedIndex; // 选中索引
	var businesscode = obj.options[index].value; // 选中值
	var req = new XMLHttpRequest();
        req.open("GET","./gongshiadd.py?businesscode="+businesscode+"&mondaytime="+mondaytime
+"&username="+username,false);
        req.send(null);
        res = req.responseText;
	res = res.replace(/\\\\/g,"\\")
	res = eval('(' + res + ')');
	allneed = res[0]
	req.open("GET","./gongshiadd1.py?businesscode="+businesscode+"&mondaytime="+mondaytime
+"&username="+username+"&businessname="+allneed.businessname+"&starttime="+allneed.starttime+"&done="+allneed.done+"&ratio="+allneed.ratio+"&businessmanager="+allneed.businessmanager+"&now="+allneed.now+"&endtime="+allneed.endtime,false);
	req.send(null);
        res = req.responseText;

	console.log(res)
	location.reload();

}


console.log(start)
window.onload=function (){//页面加载时根据本周的起始时间传入数据
        var req = new XMLHttpRequest();
        req.open("GET","./getmydata.py?start="+start+"&end="+end+"&username="+username+"&mondaytime="+mondaytime,false);
        req.send(null);
        res = req.responseText;
	res = res.replace(/\\\\/g,"\\")
	var json = eval('(' + res + ')');
	mydata = json
	req.open("GET","./getmydata01.py?username="+username+"&mondaytime="+mondaytime,false);
        req.send(null);
        res = req.responseText;
	res = res.replace(/\\\\/g,"\\")
	res = eval('(' + res + ')');
	allcode = res
	selectstr = ''
	for(let i = 0; i < allcode.length;i++){
		var passable = 0
		for(let j=0;j<mydata.length;j++){
			if(allcode[i].businesscode == mydata[j].businesscode){
				passable = 1			
			}
		}
	if(passable == 0){
		selectstr += "<option value='"+allcode[i].businesscode+"'>"+allcode[i].businesscode+"-"+allcode[i].businessname+"-"+allcode[i].businessmanager+"</option>"
		}
}

        


}

function changepassword(){
	  document.getElementById("changepwd").click();
}
function encodeUnicode(str) {  
    var res = [];  
    for ( var i=0; i<str.length; i++ ) {  
    res[i] = ( "00" + str.charCodeAt(i).toString(16) ).slice(-4);  
    }  
    return "\\u" + res.join("\\u");  
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
  	//第一个实例
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
			{type:'checkbox'},
      			{field: 'businesscode', title: '项目编码', totalRowText: '合计'}
			,{field: 'businessname', title: '项目名称'}
      			,{field: 'businessmanager', title: '项目经理'}
      			,{field: 'Monday', title:thismonday, edit:'text', totalRow: true} 
      			,{field: 'Tuesday', title: thistuesday, edit:'text', totalRow: true}
      			,{field: 'Wednesday', title:thiswednesday , edit:'text', totalRow: true}
      			,{field: 'Thursday', title:thisthursday ,edit:'text', totalRow: true}
      			,{field: 'Friday', title:thisfriday ,edit:'text', totalRow: true}
      			,{field: 'Judge', title: '审批状态'}
    		]]
      		,totalRow: true
     		,done: function (res, curr, count) {// 表格渲染完成之后的回调
			ifreload = 0
			layer.close(index);
			$("div[lay-skin='primary']")[0].remove()
	        	for (var i in res.data) {
				var item = res.data[i];
				if (item.Judge == "审批通过") {// 这里是判断需要禁用的条件（如：状态为0的）
					//$('tr[data-index=' + i + '] input[type="checkbox"]').prop('disabled', true);
					$('tr[data-index=' + i + '] td[data-edit="text"]').data('edit', null);
					$('tr[data-index=' + i + '] div[lay-skin="primary"]').remove();
				}
			}
                	count || this.elem.next('.layui-table-view').find('.layui-table-header').css('overflow', 'auto');
                	layui.each($('select'), function (index, item) {
                    	var elem = $(item);
                    	elem.val(elem.data('value')).parents('div.layui-table-cell').css('overflow', 'visible');
                	});
                $("input[lay-filter='layTableAllChoose']").prop('disabled', true);
		form.render(null, 'test1'); 
               	$("#selected").find("option[value='0']").prop("selected",true);
                $(".layui-table th").css("font-weight", "bold");// 设定表格标题字体加粗
                LayUIDataTable.SetJqueryObj($);// 第一步：设置jQuery对象
                //LayUIDataTable.HideField('num');// 隐藏列-单列模式
                //LayUIDataTable.HideField(['num','match_guest']);// 隐藏列-多列模式
                var currentRowDataList = LayUIDataTable.ParseDataTable(function (index, currentData, rowData) { })
		$.each(currentRowDataList, function (index, obj) {
                             /*
                                * 通过遍历表格集合，拿到每行数据对象obj，通过obj["列名"]["row"]可以拿到行对象，obj["列名"]["cell"]可以拿到单元格对象
                                * */
                             
                	if (obj['Judge'] && obj['Judge'].value == "审批通过") {
                                obj['Judge']["row"].css("background-color", "#ffcb00");// 对行（row）进行高亮显示
                                obj["Judge"]["cell"].css("font-weight","bold");// 对单元格（cell）字体进行加粗显示
				obj['Judge']["row"].css('disabled', true);
                            }
				
                        })
                    
  		}
	});
  setTimeout("if(ifreload==1){location.reload();}",2000)
 form.on('select(choseweek)', function(data){
	console.log(data.value)
	if(data.value == 0){
	document.getElementById("kbt1").click();
	}
	if(data.value == 1){
	document.getElementById("kbt2").click();
	}
	if(data.value == 2){
	document.getElementById("kbt3").click();
	}
	if(data.value == 3){
	document.getElementById("kbt4").click();
	}
	if(data.value == 4){
	document.getElementById("kbt5").click();
	}
  })
 $('#delRow').click(function () {
	layer.confirm('真的删除这些项目吗', function(index){
       
       var tableContainer = $('div[lay-filter="LAY-table-1"]');
        tableContainer.find('input[name="layTableCheckbox"]:checked').each(function(){
           var trDel = $(this).parents('tr');
		if(trDel[0].childNodes[4].innerText.length < 3){

	var businesscode =  trDel[0].childNodes[1].innerText
	var businessmanager =  trDel[0].childNodes[3].innerText
	var req = new XMLHttpRequest();
        req.open("GET","./gongshidelete.py?businesscode="+businesscode+"&mondaytime="+mondaytime
+"&username="+username+"&businessmanager="+businessmanager,false);
	console.log('ok')
        req.send(null);
        res = req.responseText;
	console.log(res)
            //trDel.remove();
		}
        }) 
	location.reload();
        layer.close(index);
      })


})


	$('#addRow').click(function () {
  		var index = layui.layer.open({
        title : "添加我所参与的项目",
        type : 1,
        content : 
           "      <div class='layui-row' id='test' >"
 + "        <div class='layui-col-md11'>"
+ "          <form class='layui-form' id='addEmployeeForm' lay-filter='test1'>"
+ "              "
 + "            <div class='layui-form-item'>"
 + "              <label class='layui-form-label'>项目编码：</label>"
 + "                <div class='layui-input-block'>"
 + "                  <select class='layui-input' name='deptId' id='selectbusiness'>"
 + "                    <option value=''></option>"
 + selectstr
 + "                  </select>"
+ "                </div>"
 + "            </div>"

 + "            <div class='layui-form-item'>"
  + "              <div class='layui-input-block'>"
  + "                <br/>"
  + "                <br/>"
  + "                <br/>"
  + "                <br/>"
  + "                <br/>"
  + "                <br/>"
  + "                <br/>"
  + "                <br/>"
  + "              </div>"
  + "            </div>"
+ "           <div class='layui-form-item'>"
+ "              <div class='layui-input-block'>"
 + "                <button type='button' class='layui-btn layui-btn-normal' onclick='addbusiness()'>提交</button>"
  + "              </div>"
  + "            </div>"

  + "          </form>"
  + "        </div>"
  + "      </div>"
        ,//弹出层页面
        area: ['1000px', '400px']
    })
	form.render(null, 'test1'); 
    form.on('submit(childsubmit)', function() {
        layer.close(index);
        return false
  })
		

        });
	 var _window = $(window).height();
	myheight = _window * 0.6
  	table.on('edit(test)', function(obj){
		tableIns.reload({height: myheight
    		,data : mydata 
    		,page: false
    		,limit:30
    		,cols: [[ //表头
			{type:'checkbox'},
      			{field: 'businesscode', title: '项目编码', totalRowText: '合计'}
		  	,{field: 'businessname', title: '项目名称'}
      			,{field: 'businessmanager', title: '项目经理'}
      			,{field: 'Monday', title: thismonday,edit:'text', totalRow: true} 
      			,{field: 'Tuesday', title: thistuesday,edit:'text', totalRow: true}
      			,{field: 'Wednesday', title: thiswednesday,edit:'text', totalRow: true}
      			,{field: 'Thursday', title: thisthursday,edit:'text', totalRow: true}
      			,{field: 'Friday', title: thisfriday,edit:'text', totalRow: true}
      			,{field: 'Judge', title: '审批状态'}

    		]]
		,totalRow: true
     		, done: function (res, curr, count) {// 表格渲染完成之后的回调
			$("div[lay-skin='primary']")[0].remove()
			for (var i in res.data) {
				var item = res.data[i]
				if (item.Judge == "审批通过") {// 这里是判断需要禁用的条件（如：状态为0的）
					//$('tr[data-index=' + i + '] input[type="checkbox"]').prop('disabled', true);
					$('tr[data-index=' + i + '] td[data-edit="text"]').data('edit', null);
					$('tr[data-index=' + i + '] div[lay-skin="primary"]').remove();
				}
			}
                	count || this.elem.next('.layui-table-view').find('.layui-table-header').css('overflow', 'auto');
                	layui.each($('select'), function (index, item) {
                    	var elem = $(item);
                    	elem.val(elem.data('value')).parents('div.layui-table-cell').css('overflow', 'visible');
                	});
                
			form.render(null, 'test1'); 
         		$("#selected").find("option[value='0']").prop("selected",true);
                	$(".layui-table th").css("font-weight", "bold");// 设定表格标题字体加粗

                        LayUIDataTable.SetJqueryObj($);// 第一步：设置jQuery对象

                        //LayUIDataTable.HideField('num');// 隐藏列-单列模式
                        //LayUIDataTable.HideField(['num','match_guest']);// 隐藏列-多列模式

                        var currentRowDataList = LayUIDataTable.ParseDataTable(function (index, currentData, rowData) {})
			$.each(currentRowDataList, function (index, obj) {
                             /*
                                * 通过遍历表格集合，拿到每行数据对象obj，通过obj["列名"]["row"]可以拿到行对象，obj["列名"]["cell"]可以拿到单元格对象
                                * */
                             
                            if (obj['Judge'] && obj['Judge'].value == "审批通过") {
                                obj['Judge']["row"].css("background-color", "#FAB000");// 对行（row）进行高亮显示
                                obj["Judge"]["cell"].css("font-weight","bold");// 对单元格（cell）字体进行加粗显示
				
                            }
				
                        })
                    
  		}
	});





});
});
