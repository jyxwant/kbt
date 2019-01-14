//JavaScript代码区域
layui.use('element', function(){
  var element = layui.element;
  
});

function waitforme(){
	document.getElementById("waitforme").click();
}

function kbt(){
	document.getElementById("kbt").click();
}

function validateStrAndNo(str) {
var reg = {letter:"^[A-Za-z]+$",num:"^([+-]?)\\d*\\.?\\d+$"};
if((new RegExp(reg.letter)).test(str) || (new RegExp(reg.num)).test(str)) {
return true;
}else {
return false;
}
}

layui.use('form', function(){
  var form = layui.form;
  
//监听提交


   form.on('submit(demo1)', function(data){
	var source = document.getElementById('source').value
	var thenew = document.getElementById('new').value
	var renew  = document.getElementById('renew').value
	var email  = document.getElementById('myname').innerText
        var req = new XMLHttpRequest();
	var loadlast = 0
	if(!validateStrAndNo(thenew)){
	layer.confirm('密码只能包含字母和数字', function(index){
        layer.close(index);
	location.reload();
     		 },function(index){
        layer.close(index);
	location.reload();
     		 })
	}else{
	if(thenew != renew){
	layer.confirm('两次输入的密码不一致', function(index){
        layer.close(index);
	location.reload();
     		 },function(index){
        layer.close(index);
	location.reload();
     		 })
	}
	else{
	console.log(data)
        req.open("GET","./change.py?source="+source+"&thenew="+thenew+"&email="+email,false);
	req.send(null);
        res = req.responseText;
	layer.confirm(res, function(index){
        layer.close(index);
	location.reload();
	if(res["length"] == 6){
	location.reload();}
	else{
	self.location.href='../index.html';}
	
     		 },function(index){
        layer.close(index);
	location.reload();
	if(res["length"] == 6){
	location.reload();}
	else{
	self.location.href='../index.html';}
     		 })
	}}
	return false
  });
});
