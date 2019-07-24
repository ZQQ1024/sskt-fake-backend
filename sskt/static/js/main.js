$(function(){
	$(".tli").click(function(){
		$(".tli").removeClass("on");
		$(this).addClass("on");
	});
	$("#main1").click(function(){
		$(".main").addClass("display");
		$(".main-1").removeClass("display");
		$(".talAll").addClass("display");
		$(".tal-1").removeClass("display");
	});
	$("#main2").click(function(){
		$(".main").addClass("display");
		$(".main-2").removeClass("display");
	});
	$("#main3").click(function(){
		$(".main").addClass("display");
		$(".main-3").removeClass("display");
	});
	$("#newFile").click(function(){
		$(".talAll").addClass("display");
		$(".tal-2").removeClass("display");
	});
	$("#btnNewFile").click(function(){
		$(".talAll").addClass("display");
		$(".tal-1").removeClass("display");
	});
	$(".btnZH").click(function(){
		$(".talAll").addClass("display");
		$(".tal-3").removeClass("display");
	});
	
	$("#changeTxt").click(function(){
		$(".talAll").addClass("display");
		$(".tal-4").removeClass("display");
	});
	
	$(".btnLL").click(function(){
		$(".talAll").addClass("display");
		$(".tal-5").removeClass("display");
	});
	
	$("#zhaoHui").click(function(){
		$(".talAll").addClass("display");
		$(".tal-3").removeClass("display");
	})
	
	$("#lianXi1").click(function(){
		$(".talAll").addClass("display");
		$(".tal-5").removeClass("display");
	})
	$("#lianXi2").click(function(){
		$(".talAll").addClass("display");
		$(".tal-5").removeClass("display");
	});
	
	$("#person").on("mouseenter",function(){
		$(".winTan").removeClass("display");
	});
	
	$(".winTan").on("mouseleave",function(){
		$(".winTan").addClass("display");
	})
	
	$("#logout").click(function(){
		window.location.href = "login.html";
	})
	
	var ulMainNum = 0;
	$(".ulMain").click(function(){
		if(ulMainNum == 0){
			$(this).siblings(".ulTips").addClass("display");
			ulMainNum = 1;
		}else if(ulMainNum == 1){
			$(this).siblings(".ulTips").removeClass("display");
			ulMainNum = 0;
		}
	})
})