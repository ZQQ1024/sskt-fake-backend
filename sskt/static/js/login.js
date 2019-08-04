$(function(){
	$("*").on("selectstart",function(e){
		return false; //即阻止默认行为也阻止冒泡
	})
	var locals = window.sessionStorage;
	var getV = locals.getItem("name");
	$("#name").val(getV);
	
	$("#login").click(function(){
		var name = $("#name").val();
		var pwd = $("#password").val();
		var a = {"userName":name,"passWord":pwd};
		var b = JSON.stringify(a);
		console.log(b)
		console.log(a)
		var userId = "";
		$.ajax({
			type:"POST", 
			url:"/login/",
			async:false,
			data:b,
			dataType:"JSON",
			success:function(data){
//				if(data[0] == 0){
//					userId = data[1];   
//					locals.setItem("userId",userId);
//					window.location.href="/gethttp2"; 
//				}else if(data[0] == -1){
//					alert(data[1])
//				}
				if(data.res_code == 111){
					userId = data.res_data;   
					locals.setItem("userId",userId);
					window.location.href="/index"; 
				}
			}
		});
		
	})
})
