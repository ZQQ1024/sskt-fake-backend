$(function(){
	$("*").on("selectstart",function(e){
		return false; //即阻止默认行为也阻止冒泡
	});
	var person = sessionStorage.getItem("userId");
	$("#person").html(person);
	if(person == null){
		window.location.href="/login_page/";
	}
	
	var myDate = new Date();
	//获取当前年
	var year=myDate.getFullYear();
	//获取当前月
	var month=myDate.getMonth()+1;
	$("#year").html(year);
	$("#month").html(month);
	
	
 
    
//$(document).on("datetimepicker","#rili2",function(){
//	locale: 'zh-cn'
//});
//$(document).on("datetimepicker","#rili1",function(){
// 	locale: 'zh-cn'
//});
	
	$.ajax({
        type:"get", 
        url:"/maincontent_info/",
        async:true,
        timeout:50000,
        dataType:"JSON",
        success:function(data){
        	data = data.content;
        	var rank = "";
        	var number1 = "";
        	var money = "";
        	var username = "";
        	var html = "";
        	for(var i=0;i<data.length;i++){
        		rank = data[i].rank;
        		number1 = data[i].number;
        		money = data[i].money;
        		username = data[i].username;
        		html = '<tr style="height: 50px;">'+
					       ' <td></td>'+
						    '<td>'+rank+'</td>'+
						    '<td>'+username+'</td>'+
						    '<td>'+money+'</td>'+
						    '<td>'+number1+'</td>'+
					    '</tr>';
				$("#table-11").append(html);
        	}
        }
    });

	$(".tli").click(function(){
		$(".tli").removeClass("on");
		$(this).addClass("on");
	});
	$("#main1").click(function(){
		$("#table-11").empty();
		$(".main").addClass("display");
		$(".main-1").removeClass("display");
		$(".talAll").addClass("display");
		$(".tal-1").removeClass("display");
		$.ajax({
       		type:"get", 
	        url:"/maincontent_info/",
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	data = data.content;
	        	var rank = "";
	        	var number1 = "";
	        	var money = "";
	        	var username = "";
	        	var html = "";
	        	for(var i=0;i<data.length;i++){
	        		rank = data[i].rank;
	        		number1 = data[i].number;
	        		money = data[i].money;
	        		username = data[i].username;
	        		html = '<tr style="height: 50px;">'+
						       ' <td></td>'+
							    '<td>'+rank+'</td>'+
							    '<td>'+username+'</td>'+
							    '<td>'+money+'</td>'+
							    '<td>'+number1+'</td>'+
						    '</tr>';
					$("#table-11").append(html);
	        	}
	        }
	    });
	});
	$("#main2").click(function(){
		$("#table-41").empty();
		$(".main").addClass("display");
		$(".main-2").removeClass("display");
		$.ajax({
	        type:"get", 
	        url:"/applications_info/",
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	console.log(data)
	        	data = data.apps_info;
	        	var manager_number = "";
	        	var manager_name = "";
	        	var manager_phone = "";
	        	var item_name = "";
	        	var item_number = "";
	        	var status = "";
	        	var seller = "";
	        	var recorder = "";
	        	var update_person = "";
	        	var update_time = "";
	        	var commit_time = "";
	        	var specify_flag = "";
	        	var html = "";
	        	var statu1 = "";
	        	for(var i=0;i<data.length;i++){
	        		manager_number = data[i].manager_number;
	        		manager_name = data[i].manager_name;
	        		manager_phone = data[i].manager_phone;
	        		item_name = data[i].item_name;
	        		item_number = data[i].item_number;
	        		status = data[i].status;
	        		seller = data[i].seller;
	        		recorder = data[i].recorder;
	        		update_person = data[i].update_person;
	        		update_time = data[i].update_time;
	        		commit_time = data[i].commit_time;
	        		specify_flag = data[i].specify_flag;
	        		console.log(specify_flag)
	        		if(status == 0){
						statu1 = "未确认";
					}else if(status == 1){
						statu1 = "审查中";
					}else if(status == 2){
						statu1 = "审查失败";
					}else if(status == 3){
						statu1 = "等待入金";
					}else if(status == 4){
						statu1 = "契约完了";
					}else if(status == 5){
						statu1 = "入金完了";
					};
					if(specify_flag == "NORMAL"){
						html = '<tr>'+
							    '<td class="ssktNm">'+manager_number+'</td>'+
							    '<td>'+manager_name+'</td>'+
							    '<td>'+manager_phone+'</td>'+
							    '<td>'+item_name+'</td>'+
							    '<td>'+item_number+'</td>'+
							    '<td>'+statu1+'</td>'+
							    '<td>'+seller+'</td>'+
							    '<td>'+recorder+'</td>'+
							    '<td>'+update_person+'</td>'+
							    '<td>'+update_time+'</td>'+
							    '<td>'+commit_time+'</td>'+
							    '<td>'+
							    	'<button class="btn btn-success btn-xs btnZH">照会</button>'+
									'<button class="btn btn-primary btn-xs btnLL">联络</button>'+
							    '</td>'+
						    '</tr>';
					}else if(specify_flag == "RED"){
						html = '<tr style="background: red;">'+
							    '<td class="ssktNm">'+manager_number+'</td>'+
							    '<td>'+manager_name+'</td>'+
							    '<td>'+manager_phone+'</td>'+
							    '<td>'+item_name+'</td>'+
							    '<td>'+item_number+'</td>'+
							    '<td>'+statu1+'</td>'+
							    '<td>'+seller+'</td>'+
							    '<td>'+recorder+'</td>'+
							    '<td>'+update_person+'</td>'+
							    '<td>'+update_time+'</td>'+
							    '<td>'+commit_time+'</td>'+
							    '<td>'+
							    	'<button class="btn btn-success btn-xs btnZH">照会</button>'+
									'<button class="btn btn-primary btn-xs btnLL">联络</button>'+
							    '</td>'+
						    '</tr>';
					}
	        		
					$("#table-41").append(html);
	        	}
	        }
	    });
	});
	$("#main3").click(function(){
		$("#fileAll").empty();
		$(".main").addClass("display");
		$(".main-3").removeClass("display");
		$.ajax({
	        type:"get", 
	        url:"/get_all_ssktnum/",
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	$("#allSskt").empty();
	        	data = data.res;
	        	for(var i = 0;i<data.length;i++){
	        		var html = '<option>'+data[i]+'</option>';
	        		$("#allSskt").append(html);
	        	}
	        }
    	});
    	
		$.ajax({
	        type:"get", 
	        url:"/doc/",
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	data = data.content;
	        	console.log(data)
	        	var SSKTName = "";
	        	var file_string = "";
	        	var html = "";
	        	for(var i = 0;i<data.length;i++){
	        		SSKTName = data[i].SSKT_number;
	        		file_string = data[i].file_string;
	        		var html1 = "";
	        		for(var j = 0;j<file_string.length;j++){
	        			html1 += '<a href="'+file_string[j]+'" download=""><li class="ulTips" style="margin-left: 60px;"><i class="fa fa-folder-open-o" style="color: #2AABD2;"></i>&nbsp;&nbsp;&nbsp;'+file_string[j]+'</li></a>';
	        		}
	        		html = '<ul style="padding: 0;margin-top: 10px;">'+
	    						'<li class="ulMain" style="margin-left: 20px;"><i class="fa fa-folder-open-o" style="color: #2AABD2;"></i>&nbsp;&nbsp;&nbsp;'+SSKTName+'</li>'+html1+
	    					'</ul>';
	    			$("#fileAll").append(html);
	    			
	        	}
	        	
	        }
    	});
	});
	//追加文件
	$("#sendfile").click(function(){
		var allSskt = $("#allSskt").val();
		var formData = new FormData();
		formData.append("ssktnum",allSskt);
		formData.append("file",$("#addFile_1")[0].files[0]);
		$.ajax({
	        type:"POST", 
	        url:"/file_addto/",
	        data:formData,
	        processData: false,
   			contentType: false,
	        timeout:50000,
	        success:function(data){
	        	$("#fileAll").empty();
	        	$.ajax({
			        type:"get", 
			        url:"/doc/",
			        async:true,
			        timeout:50000,
			        dataType:"JSON",
			        success:function(data){
			        	data = data.content;
			        	console.log(data)
			        	var SSKTName = "";
			        	var file_string = "";
			        	var html = "";
			        	for(var i = 0;i<data.length;i++){
			        		SSKTName = data[i].SSKT_number;
			        		file_string = data[i].file_string;
			        		var html1 = "";
			        		for(var j = 0;j<file_string.length;j++){
			        			html1 += '<a href="'+file_string[j]+'" download=""><li class="ulTips" style="margin-left: 60px;"><i class="fa fa-folder-open-o" style="color: #2AABD2;"></i>&nbsp;&nbsp;&nbsp;'+file_string[j]+'</li></a>';
			        		}
			        		html = '<ul style="padding: 0;margin-top: 10px;">'+
			    						'<li class="ulMain" style="margin-left: 20px;"><i class="fa fa-folder-open-o" style="color: #2AABD2;"></i>&nbsp;&nbsp;&nbsp;'+SSKTName+'</li>'+html1+
			    					'</ul>';
			    			$("#fileAll").append(html);
			    			
			        	}
			        	
			        }
		    	});
	        }
    	});
	})
	
	$("#newFile").click(function(){
		$(".talAll").addClass("display");
		$(".tal-2").removeClass("display");
	});
//	$("#btnNewFile").click(function(){
//		
//	});
	$(document).on("click",".btnZH",function(){
		var ssktNm = $(this).parents("tr").children(".ssktNm").html();
		$(".talAll").addClass("display");
		$(".tal-3").removeClass("display");
		$(".xiuz").empty();
		var c = {"sskt_num" : ssktNm};
		$.ajax({
	        type:"get", 
	        url:"/applications_info_detail/",
	        data:c,
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	console.log(data);
	        	var UserNameWrite = data.UserNameWrite;
				var UserNameAlias = data.UserNameAlias;
				var UserNameRead =data.UserNameRead;
				var UserAddr =data.UserAddr ;
				var UserAddrPostCode =data.UserAddrPostCode ;
				var UserPhone = data.UserPhone;
				var ManagerCompanyName =data.ManagerCompanyName ;
				var ManagerCompanyAddr =data.ManagerCompanyAddr;
				var ManagerCompanyChargerName = data.ManagerCompanyChargerName;
				var ManagerCompanyPhone =data.ManagerCompanyPhone;
				var ThingName =data.ThingName ;
				var ThingNumber = data.ThingNumber;
				var ThingStructI = data.ThingStructI;
				var ThingStructII =data.ThingStructII;
				var ThingArea = data.ThingArea;
				var ThingStayPeopleNumber =data.ThingStayPeopleNumber ;
				var ThingAddr =data.ThingAddr ;
				var ThingAddrPostcode =data.ThingAddrPostcode ;
				var ThingRentCost = data.ThingRentCost;
				var ThingManageCost = data.ThingManageCost;
				var ThingGiftCost = data.ThingGiftCost;
				var ThingDepositCost = data.ThingDepositCost;
				var ThingReliefCost = data.ThingReliefCost;
				var SettlementDate = data.SettlementDate;
				var ContractDate =data.ContractDate;
				var AD = data.AD;
				var AgencyFee = data.AgencyFee;
				var BackFee = data.BackFee
				var tip = data.tip
				var html = '<div class="row" style="margin: 0;margin-top: 20px;">'+
								'<p id="sskt123" class="display">'+ssktNm+'</p>'+
		    					'<h4 style="margin-left:58px;">契约者</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addName1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserNameWrite+'"/>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">姓名</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addName2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserNameAlias+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">名字假名</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName3a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserNameRead+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">名字拼音</p></div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName4a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserAddr+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">当前详细地址</p></div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName5a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserAddrPostCode+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">当前邮政编码</p></div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName6a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserPhone+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">电话号码</p></div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">贷主情报（管理会社）</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addMan1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ManagerCompanyName+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司名称</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMan2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ManagerCompanyAddr+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司地址</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMan3a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ManagerCompanyChargerName+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司负责人名称</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMan4a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ManagerCompanyPhone+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司电话号码</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    				'	<h4 style="margin-left:58px;">物件情报</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addThing1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingName+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">物件名</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingNumber+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">号室</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing3a" style="width: 650px;float: right;margin-right: 360px;"  disabled="disabled" placeholder="'+ThingStructI+'"/>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">结构1</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing4a" style="width: 650px;float: right;margin-right: 360px;"  disabled="disabled" placeholder="'+ThingStructII+'"/>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">结构2</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing5a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingArea+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">面积</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing6a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingStayPeopleNumber+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">入住人数</p>'+
		    				'	</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing7a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingAddr+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">所在地详细地址</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing8a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingAddrPostcode+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">所在地邮政编码</p>'+
		    					'</div>'+
		    				'	<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing9a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingRentCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">租金（每月）</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing10a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingManageCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理费用（每月）</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing11a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingGiftCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">礼金</p>'+
		    				'	</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing12a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingDepositCost+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">敷金</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing13a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingReliefCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">保证金</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">入契日情报</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addTime1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+SettlementDate+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">入住日</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addTime2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ContractDate+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">合同日</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">报酬</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addMony1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+AD+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">AD</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMony2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+AgencyFee+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">中介费</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMony3a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+BackFee+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">返金</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;margin-bottom: 20px;">'+
		    					'<h4 style="margin-left:58px;">备注</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<textarea id="addBeia" style="width: 650px;float: right;margin-right: 360px;height: 100px;resize: none;"  disabled="disabled" placeholder="'+tip+'"/></textarea>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">备注</p>'+
		    					'</div>'+
		    				'</div>'+
				    		'<button type="button" class="btn btn-default buttonLX" id="lianXi1">联系</button>';
				$(".xiuz").append(html);   	
	        }
    	});
	});
	
	$("#changeTxt").click(function(){
		$(".xiuG").empty();
		var ssktNm = $("#sskt123").html();
		var c = {"sskt_num" : ssktNm};
		$.ajax({
	        type:"get", 
	        url:"/applications_info_detail/",
	        data:c,
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	$(".talAll").addClass("display");
				$(".tal-4").removeClass("display");
	        	var UserNameWrite = data.UserNameWrite;
				var UserNameAlias = data.UserNameAlias;
				var UserNameRead =data.UserNameRead;
				var UserAddr =data.UserAddr ;
				var UserAddrPostCode =data.UserAddrPostCode ;
				var UserPhone = data.UserPhone;
				var ManagerCompanyName =data.ManagerCompanyName ;
				var ManagerCompanyAddr =data.ManagerCompanyAddr;
				var ManagerCompanyChargerName = data.ManagerCompanyChargerName;
				var ManagerCompanyPhone =data.ManagerCompanyPhone;
				var ThingName =data.ThingName ;
				var ThingNumber = data.ThingNumber;
				var ThingStructI = data.ThingStructI;
				var ThingStructII =data.ThingStructII;
				var ThingArea = data.ThingArea;
				var ThingStayPeopleNumber =data.ThingStayPeopleNumber ;
				var ThingAddr =data.ThingAddr ;
				var ThingAddrPostcode =data.ThingAddrPostcode ;
				var ThingRentCost = data.ThingRentCost;
				var ThingManageCost = data.ThingManageCost;
				var ThingGiftCost = data.ThingGiftCost;
				var ThingDepositCost = data.ThingDepositCost;
				var ThingReliefCost = data.ThingReliefCost;
				var SettlementDate = data.SettlementDate;
				var ContractDate =data.ContractDate;
				var AD = data.AD;
				var AgencyFee = data.AgencyFee;
				var BackFee = data.BackFee
				var tip = data.tip
				var html = '<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">契约者</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addName1c" style="width: 650px;float: right;margin-right: 360px;" value="'+UserNameWrite+'"/>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">姓名</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addName2c" style="width: 650px;float: right;margin-right: 360px;" value="'+UserNameAlias+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">名字假名</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName3c" style="width: 650px;float: right;margin-right: 360px;" value="'+UserNameRead+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">名字拼音</p></div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName4c" style="width: 650px;float: right;margin-right: 360px;" value="'+UserAddr+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">当前详细地址</p></div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName5c" style="width: 650px;float: right;margin-right: 360px;" value="'+UserAddrPostCode+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">当前邮政编码</p></div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName6c" style="width: 650px;float: right;margin-right: 360px;" value="'+UserPhone+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">电话号码</p></div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">贷主情报（管理会社）</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addMan1c" style="width: 650px;float: right;margin-right: 360px;" value="'+ManagerCompanyName+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司名称</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMan2c" style="width: 650px;float: right;margin-right: 360px;" value="'+ManagerCompanyAddr+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司地址</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMan3c" style="width: 650px;float: right;margin-right: 360px;" value="'+ManagerCompanyChargerName+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司负责人名称</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMan4c" style="width: 650px;float: right;margin-right: 360px;" value="'+ManagerCompanyPhone+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司电话号码</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    				'	<h4 style="margin-left:58px;">物件情报</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addThing1c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingName+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">物件名</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing2c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingNumber+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">号室</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing3c" style="width: 650px;float: right;margin-right: 360px;"  value="'+ThingStructI+'"/>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">结构1</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing4c" style="width: 650px;float: right;margin-right: 360px;"  value="'+ThingStructII+'"/>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">结构2</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing5c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingArea+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">面积</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing6c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingStayPeopleNumber+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">入住人数</p>'+
		    				'	</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing7c" style="width: 650px;float: right;margin-right: 360px;"  value="'+ThingAddr+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">所在地详细地址</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing8c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingAddrPostcode+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">所在地邮政编码</p>'+
		    					'</div>'+
		    				'	<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing9c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingRentCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">租金（每月）</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing10c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingManageCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理费用（每月）</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing11c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingGiftCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">礼金</p>'+
		    				'	</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing12c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingDepositCost+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">敷金</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing13c" style="width: 650px;float: right;margin-right: 360px;" value="'+ThingReliefCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">保证金</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">入契日情报</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<div class="input-group date" id="rili1" data-target-input="nearest" style="float: right;margin-right: 330px;">'+
		    							 '<div class="input-group-append" data-target="#rili1" data-toggle="datetimepicker" style="float: right;">'+
					                       ' <div class="input-group-text"><i class="fa fa-calendar" style="font-size: 18px;line-height: 35px;margin-left: 15px;"></i></div>'+
					                   ' </div>'+
					                    '<input id="addTime1c" type="text" class="form-control datetimepicker-input" style="width: 650px;float: right;" data-target="#rili1" value="'+SettlementDate+'"/>'+
					                '</div>'+
					                '<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">入住日</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<div class="input-group date" id="rili2" data-target-input="nearest" style="float: right;margin-right: 330px;">'+
		    							' <div class="input-group-append" data-target="#rili2" data-toggle="datetimepicker" style="float: right;">'+
					                        '<div class="input-group-text"><i class="fa fa-calendar" style="font-size: 18px;line-height: 35px;margin-left: 15px;"></i></div>'+
					                    '</div>'+
					                   ' <input id="addTime2c" type="text" class="form-control datetimepicker-input" style="width: 650px;float: right;" data-target="#rili2" value="'+ContractDate+'"/>'+
					                '</div>'+
					               ' <p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">合同日</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">报酬</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addMony1c" style="width: 650px;float: right;margin-right: 360px;" value="'+AD+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">AD</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMony2c" style="width: 650px;float: right;margin-right: 360px;" value="'+AgencyFee+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">中介费</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMony3c" style="width: 650px;float: right;margin-right: 360px;" value="'+BackFee+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">返金</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;margin-bottom: 20px;">'+
		    					'<h4 style="margin-left:58px;">备注</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<textarea id="addBeic" style="width: 650px;float: right;margin-right: 360px;height: 100px;resize: none;" value="'+tip+'"/></textarea>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">备注</p>'+
		    					'</div>'+
		    				'</div>'+
				    		'<button type="button" class="btn btn-default buttonLX" id="lianXi1">联系</button>';
				$(".xiuG").append(html);   	
	        }
    	});
	});
	
	
	$(document).on("click",".cansle",function(){
		console.log("11")
		$(".main").addClass("display");
		$(".main-2").removeClass("display");
		$(".talAll").addClass("display");
		$(".tal-1").removeClass("display");
	})
	
	$('#addFile').change(function(e){
        var fileMsg = e.currentTarget.files;
        var fileName = fileMsg[0].name;
        console.log(fileName)
        $("#addfiletext").val(fileName);
    });
   
    $('#addFile_1').change(function(e){
        var fileMsg = e.currentTarget.files;
        var fileName = fileMsg[0].name;
        console.log(fileName)
        $("#addfiletext_1").val(fileName);
    });
	
	$(document).on("click",".btnLL",function(){
		$("#table-31").empty();
		var ssktNm = $(this).parents("tr").children(".ssktNm").html();
		var c = {"sskt_num" : ssktNm};
		var html1 = '<p id="sskt321" class="display">'+ssktNm+'</p>';
		$.ajax({
	        type:"get", 
	        url:"/comment_info/",
	        data:c,
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	$(".talAll").addClass("display");
				$(".tal-5").removeClass("display");
	        	data = data.comments_info;
	        	var html = "";
	        	for(var i = 0;i<data.length;i++){
	        		var Comment_id = data[i].Comment_id;
		        	var Content = data[i].Content;
		        	var CreatePerson = data[i].CreatePerson;
		        	var CreateDate = data[i].CreateDate;
		        	var UpdatePerson = data[i].UpdatePerson;
		        	var UpdateDate = data[i].UpdateDate;
		        	var Status = data[i].Status;
		        	if(Status == "unchecked"){
		        		html =  '<tr>'+
		        					'<td class="comment_id" style="display:none;">'+Comment_id+'</td>'+
								    '<td style="width: 400px;">'+Content+'</td>'+
								    '<td>'+CreatePerson+'</td>'+
								    '<td>'+CreateDate+'</td>'+
								    '<td>'+UpdatePerson+'</td>'+
								    '<td>'+UpdateDate+'</td>'+
								    '<td><button class="btn btnCek">完成</button></td>'+
							    '</tr>';
		        	}else{
		        		html =  '<tr>'+
								    '<td class="comment_id" style="dispaly:none;">'+Comment_id+'</td>'+
								    '<td style="width: 400px;">'+Content+'</td>'+
								    '<td>'+CreatePerson+'</td>'+
								    '<td>'+CreateDate+'</td>'+
								    '<td>'+UpdatePerson+'</td>'+
								    '<td>'+UpdateDate+'</td>'+
								    '<td><button disabled="disabled" class="btn btnCek">完成</button></td>'+
							    '</tr>';
		        	}
		        	$("#table-31").append(html);
	        	}
	        	$("#table-31").append(html1);
	        }
    	});
	});
	
	$(document).on("click",".btnCek",function(){
		var comment_id =  $(this).parent("td").siblings('.comment_id').html();
		console.log(comment_id)
		var c = {"Comment_id" : comment_id};
		var b = JSON.stringify(c);
		$.ajax({
	        type:"POST", 
	        url:"/confirm_comment/",
	        data:b,
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	alert("确认成功");
	        }
    	});
	})
	
	$("#zhaoHui").click(function(){
		var ssktNm = $("#sskt321").html();
		$(".xiuz").empty();
		var c = {"sskt_num" : ssktNm};
		$.ajax({
	        type:"get", 
	        url:"/applications_info_detail/",
	        data:c,
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	$(".talAll").addClass("display");
				$(".tal-3").removeClass("display");
	        	var UserNameWrite = data.UserNameWrite;
				var UserNameAlias = data.UserNameAlias;
				var UserNameRead =data.UserNameRead;
				var UserAddr =data.UserAddr ;
				var UserAddrPostCode =data.UserAddrPostCode ;
				var UserPhone = data.UserPhone;
				var ManagerCompanyName =data.ManagerCompanyName ;
				var ManagerCompanyAddr =data.ManagerCompanyAddr;
				var ManagerCompanyChargerName = data.ManagerCompanyChargerName;
				var ManagerCompanyPhone =data.ManagerCompanyPhone;
				var ThingName =data.ThingName ;
				var ThingNumber = data.ThingNumber;
				var ThingStructI = data.ThingStructI;
				var ThingStructII =data.ThingStructII;
				var ThingArea = data.ThingArea;
				var ThingStayPeopleNumber =data.ThingStayPeopleNumber ;
				var ThingAddr =data.ThingAddr ;
				var ThingAddrPostcode =data.ThingAddrPostcode ;
				var ThingRentCost = data.ThingRentCost;
				var ThingManageCost = data.ThingManageCost;
				var ThingGiftCost = data.ThingGiftCost;
				var ThingDepositCost = data.ThingDepositCost;
				var ThingReliefCost = data.ThingReliefCost;
				var SettlementDate = data.SettlementDate;
				var ContractDate =data.ContractDate;
				var AD = data.AD;
				var AgencyFee = data.AgencyFee;
				var BackFee = data.BackFee
				var tip = data.tip
				var html = '<div class="row" style="margin: 0;margin-top: 20px;">'+
								'<p id="sskt123" class="display">'+ssktNm+'</p>'+
		    					'<h4 style="margin-left:58px;">契约者</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addName1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserNameWrite+'"/>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">姓名</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addName2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserNameAlias+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">名字假名</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName3a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserNameRead+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">名字拼音</p></div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName4a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserAddr+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">当前详细地址</p></div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName5a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserAddrPostCode+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">当前邮政编码</p></div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;"><input id="addName6a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+UserPhone+'" /><p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">电话号码</p></div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">贷主情报（管理会社）</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addMan1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ManagerCompanyName+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司名称</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMan2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ManagerCompanyAddr+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司地址</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMan3a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ManagerCompanyChargerName+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司负责人名称</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMan4a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ManagerCompanyPhone+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理公司电话号码</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    				'	<h4 style="margin-left:58px;">物件情报</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addThing1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingName+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">物件名</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingNumber+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">号室</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing3a" style="width: 650px;float: right;margin-right: 360px;"  disabled="disabled" placeholder="'+ThingStructI+'"/>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">结构1</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing4a" style="width: 650px;float: right;margin-right: 360px;"  disabled="disabled" placeholder="'+ThingStructII+'"/>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">结构2</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing5a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingArea+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">面积</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing6a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingStayPeopleNumber+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">入住人数</p>'+
		    				'	</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing7a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingAddr+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">所在地详细地址</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing8a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingAddrPostcode+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">所在地邮政编码</p>'+
		    					'</div>'+
		    				'	<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'	<input id="addThing9a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingRentCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">租金（每月）</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing10a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingManageCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">管理费用（每月）</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing11a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingGiftCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">礼金</p>'+
		    				'	</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing12a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingDepositCost+'" />'+
		    					'	<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">敷金</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addThing13a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ThingReliefCost+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">保证金</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">入契日情报</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addTime1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+SettlementDate+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">入住日</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addTime2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+ContractDate+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">合同日</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    					'<h4 style="margin-left:58px;">报酬</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<input id="addMony1a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+AD+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">AD</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMony2a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+AgencyFee+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">中介费</p>'+
		    					'</div>'+
		    					'<div class="row" style="margin: 0;margin-top: 20px;">'+
		    						'<input id="addMony3a" style="width: 650px;float: right;margin-right: 360px;" disabled="disabled" placeholder="'+BackFee+'" />'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">返金</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;margin-top: 20px;margin-bottom: 20px;">'+
		    					'<h4 style="margin-left:58px;">备注</h4>'+
		    					'<div class="row" style="margin: 0;">'+
		    						'<textarea id="addBeia" style="width: 650px;float: right;margin-right: 360px;height: 100px;resize: none;"  disabled="disabled" placeholder="'+tip+'"/></textarea>'+
		    						'<p style="float: right;margin: 0;line-height: 26px;font-size: 16px;font-weight: bold;margin-right: 40px;">备注</p>'+
		    					'</div>'+
		    				'</div>'+
		    				'<div class="row" style="margin: 0;display: flex;align-items: center;justify-content: center;margin-top: 20px;margin-bottom: 20px;">'+
				    			'<button class="btn cansle" style="background-color:#00BBE9;margin-left: 40px;">取消</button>'+
				    		'</div>'+
				    		'<button type="button" class="btn btn-default buttonLX" id="lianXi1">联系</button>';
				$(".xiuz").append(html);   	
	        }
    	});
	})
	
	$(document).on("click","#lianXi1",function(){
		var ssktNm = $("#sskt123").html();
		$("#table-31").empty();
		var c = {"sskt_num" : ssktNm};
		var html1 = '<p id="sskt321" class="display">'+ssktNm+'</p>';
		$.ajax({
	        type:"get", 
	        url:"/comment_info/",
	        data:c,
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	$(".talAll").addClass("display");
				$(".tal-5").removeClass("display");
	        	data = data.comments_info;
	        	var html = "";
	        	for(var i = 0;i<data.length;i++){
	        		var Comment_id = data[i].Comment_id;
		        	var Content = data[i].Content;
		        	var CreatePerson = data[i].CreatePerson;
		        	var CreateDate = data[i].CreateDate;
		        	var UpdatePerson = data[i].UpdatePerson;
		        	var UpdateDate = data[i].UpdateDate;
		        	var Status = data[i].Status;
		        	if(Status == "unchecked"){
		        		html =  '<tr>'+
		        					'<td class="comment_id" style="display:none;">'+Comment_id+'</td>'+
								    '<td style="width: 400px;">'+Content+'</td>'+
								    '<td>'+CreatePerson+'</td>'+
								    '<td>'+CreateDate+'</td>'+
								    '<td>'+UpdatePerson+'</td>'+
								    '<td>'+UpdateDate+'</td>'+
								    '<td><button class="btn btnCek">完成</button></td>'+
							    '</tr>';
		        	}else{
		        		html =  '<tr>'+
								    '<td class="comment_id" style="dispaly:none;">'+Comment_id+'</td>'+
								    '<td style="width: 400px;">'+Content+'</td>'+
								    '<td>'+CreatePerson+'</td>'+
								    '<td>'+CreateDate+'</td>'+
								    '<td>'+UpdatePerson+'</td>'+
								    '<td>'+UpdateDate+'</td>'+
								    '<td><button disabled="disabled" class="btn btnCek">完成</button></td>'+
							    '</tr>';
		        	}
		        	$("#table-31").append(html);
	        	}
	        	$("#table-31").append(html1);
	        }
    	});
	})
	$("#lianXi2").click(function(){
		alert("修改中无法使用")
	});
	
	$("#person").on("mouseenter",function(){
		$(".winTan").removeClass("display");
	});
	
	$(".winTan").on("mouseleave",function(){
		$(".winTan").addClass("display");
	})
	
	
	var ulMainNum = 0;
	$(document).on("click",".ulMain",function(){
		if(ulMainNum == 0){
			$(this).siblings(".ulTips").addClass("display");
			ulMainNum = 1;
		}else if(ulMainNum == 1){
			$(this).siblings(".ulTips").removeClass("display");
			ulMainNum = 0;
		}
	});
	//新建
	$("#btnNewFile").click(function(){
		var UserNameWrite = $("#addName1").val();
		var UserNameAlias = $("#addName2").val();
		var UserNameRead = $("#addName3").val();
		var UserAddr = $("#addName4").val();
		var UserAddrPostCode = $("#addName5").val();
		var UserPhone = $("#addName6").val();
		var ManagerCompanyName = $("#addMan1").val();
		var ManagerCompanyAddr = $("#addMan2").val();
		var ManagerCompanyChargerName = $("#addMan3").val();
		var ManagerCompanyPhone = $("#addMan4").val();
		var ThingName = $("#addThing1").val();
		var ThingNumber = $("#addThing2").val();
		var ThingStructI = $("#addThing3").val();
		var ThingStructII = $("#addThing4").val();
		var ThingArea = $("#addThing5").val();
		var ThingStayPeopleNumber = $("#addThing6").val();
		var ThingAddr = $("#addThing7").val();
		var ThingAddrPostcode = $("#addThing8").val();
		var ThingRentCost = $("#addThing9").val();
		var ThingManageCost = $("#addThing10").val();
		var ThingGiftCost = $("#addThing11").val();
		var ThingDepositCost = $("#addThing12").val();
		var ThingReliefCost = $("#addThing13").val();
		var SettlementDate = $("#addTime1").val();
		var ContractDate = $("#addTime2").val();
		var ADc = $("#addMony1").val();
		var AgencyFee = $("#addMony2").val();
		var BackFee = $("#addMony3").val();
		var tip = $("#addBei").val();
		var formData = new FormData();
		formData.append("UserNameWrite",UserNameWrite);
		formData.append("UserNameAlias",UserNameAlias);
		formData.append("UserNameRead",UserNameRead);
		formData.append("UserAddr",UserAddr);
		formData.append("UserAddrPostCode",UserAddrPostCode);
		formData.append("UserPhone",UserPhone);
		formData.append("ManagerCompanyName",ManagerCompanyName);
		formData.append("ManagerCompanyAddr",ManagerCompanyAddr);
		formData.append("ManagerCompanyChargerName",ManagerCompanyChargerName);
		formData.append("ManagerCompanyPhone",ManagerCompanyPhone);
		formData.append("ThingName",ThingName);
		formData.append("ThingNumber",ThingNumber);
		formData.append("ThingStructI",ThingStructI);
		formData.append("ThingStructII",ThingStructII);
		formData.append("ThingArea",ThingArea);
		formData.append("ThingStayPeopleNumber",ThingStayPeopleNumber);
		formData.append("ThingAddr",ThingAddr);
		formData.append("ThingAddrPostcode",ThingAddrPostcode);
		formData.append("ThingRentCost",ThingRentCost);
		formData.append("ThingManageCost",ThingManageCost);
		formData.append("ThingGiftCost",ThingGiftCost);
		formData.append("ThingDepositCost",ThingDepositCost);
		formData.append("ThingReliefCost",ThingReliefCost);
		formData.append("SettlementDate",SettlementDate);
		formData.append("ContractDate",ContractDate);
		formData.append("AD",ADc);
		formData.append("AgencyFee",AgencyFee);
		formData.append("BackFee",BackFee);
		formData.append("tip",tip);
		formData.append("file",$("#addFile")[0].files[0]);
		$.ajax({
	        type:"POST", 
	        url:"/commit_app/",
	        data:formData,
	        processData: false,
   			contentType: false,
	        timeout:50000,
	        success:function(data){
	        	if(data.res_code == 312){
	        		alert("创建成功");
					window.location.reload();	        		
	        	}
				else{
           			alert("输入有误请确认");
          		}
	        }
    	});
	});
	
	$("#changgeS").click(function(){
		var UserNameWrite = $("#addName1c").val();
		var UserNameAlias = $("#addName2c").val();
		var UserNameRead = $("#addName3c").val();
		var UserAddr = $("#addName4c").val();
		var UserAddrPostCode = $("#addName5c").val();
		var UserPhone = $("#addName6c").val();
		var ManagerCompanyName = $("#addMan1c").val();
		var ManagerCompanyAddr = $("#addMan2c").val();
		var ManagerCompanyChargerName = $("#addMan3c").val();
		var ManagerCompanyPhone = $("#addMan4c").val();
		var ThingName = $("#addThing1c").val();
		var ThingNumber = $("#addThing2c").val();
		var ThingStructI = $("#addThing3c").val();
		var ThingStructII = $("#addThing4c").val();
		var ThingArea = $("#addThing5c").val();
		var ThingStayPeopleNumber = $("#addThing6c").val();
		var ThingAddr = $("#addThing7c").val();
		var ThingAddrPostcode = $("#addThing8c").val();
		var ThingRentCost = $("#addThing9c").val();
		var ThingManageCost = $("#addThing10c").val();
		var ThingGiftCost = $("#addThing11c").val();
		var ThingDepositCost = $("#addThing12c").val();
		var ThingReliefCost = $("#addThing13c").val();
		var SettlementDate = $("#addTime1c").val();
		var ContractDate = $("#addTime2c").val();
		var ADc = $("#addMony1c").val();
		var AgencyFee = $("#addMony2c").val();
		var BackFee = $("#addMony3c").val();
		var tip = $("#addBeic").val();
		var formData = new FormData();
		var ssktNm = $("#sskt123").html();
		formData.append("sskt_num",ssktNm)
		formData.append("UserNameWrite",UserNameWrite);
		formData.append("UserNameAlias",UserNameAlias);
		formData.append("UserNameRead",UserNameRead);
		formData.append("UserAddr",UserAddr);
		formData.append("UserAddrPostCode",UserAddrPostCode);
		formData.append("UserPhone",UserPhone);
		formData.append("ManagerCompanyName",ManagerCompanyName);
		formData.append("ManagerCompanyAddr",ManagerCompanyAddr);
		formData.append("ManagerCompanyChargerName",ManagerCompanyChargerName);
		formData.append("ManagerCompanyPhone",ManagerCompanyPhone);
		formData.append("ThingName",ThingName);
		formData.append("ThingNumber",ThingNumber);
		formData.append("ThingStructI",ThingStructI);
		formData.append("ThingStructII",ThingStructII);
		formData.append("ThingArea",ThingArea);
		formData.append("ThingStayPeopleNumber",ThingStayPeopleNumber);
		formData.append("ThingAddr",ThingAddr);
		formData.append("ThingAddrPostcode",ThingAddrPostcode);
		formData.append("ThingRentCost",ThingRentCost);
		formData.append("ThingManageCost",ThingManageCost);
		formData.append("ThingGiftCost",ThingGiftCost);
		formData.append("ThingDepositCost",ThingDepositCost);
		formData.append("ThingReliefCost",ThingReliefCost);
		formData.append("SettlementDate",SettlementDate);
		formData.append("ContractDate",ContractDate);
		formData.append("AD",ADc);
		formData.append("AgencyFee",AgencyFee);
		formData.append("BackFee",BackFee);
		formData.append("tip",tip);
		$.ajax({
	        type:"POST", 
	        url:"/app_info_update/",
	        data:formData,
	        processData: false,
   			contentType: false,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	if(data.res_code == 31221){
	        		alert("修改成功");
					window.location.reload();	        		
	        	}else{
	        		alert("修改失败");
	        	}
	        }
    	});
	})
	
	$("#addChatBtn").click(function(){
		var addChat = $("#addChat").val();
		console.log(addChat);
		if(addChat == ""){
			alert("没有内容");
		}else{
			var ssktNm = $("#sskt321").html();
			var c = {"sskt_num":ssktNm,"Content":addChat};
			var b = JSON.stringify(c);
			$.ajax({
		        type:"POST", 
		        url:"/commit_comment_msg/",
		        data:b,
		        timeout:50000,
		        dataType:"JSON",
		        success:function(data){
		        	data = data.res_data;
		        	var Comment_id = data.Comment_id;
		        	var Content = data.Content;
		        	var CreatePerson = data.CreatePerson;
		        	var CreateDate = data.CreateDate;
		        	var UpdatePerson = data.UpdatePerson;
		        	var UpdateDate = data.UpdateDate;
		        	var Status = data.Status;
	        		var html =  '<tr>'+
	        					'<td class="comment_id" style="display:none;">'+Comment_id+'</td>'+
							    '<td style="width: 400px;">'+Content+'</td>'+
							    '<td>'+CreatePerson+'</td>'+
							    '<td>'+CreateDate+'</td>'+
							    '<td>'+UpdatePerson+'</td>'+
							    '<td>'+UpdateDate+'</td>'+
							    '<td><button class="btn btnCek">完成</button></td>'+
						    '</tr>';
		        	alert("留言成功")
		        	$("#table-31").append(html);
		        	document.getElementById("addChat").value="";
		        }
	    	});
		}
	});
	
	//登出
	
	$("#logout").click(function(){
		$.ajax({
       		type:"POST", 
	        url:"/logout/",
	        async:true,
	        timeout:50000,
	        dataType:"JSON",
	        success:function(data){
	        	window.location.href="/login_page/";
	        }
	    });
	});
})