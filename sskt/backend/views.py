from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ApplicationRecord, House, Company, Reward, Live, Tip, Renter
from datetime import datetime

import json

# Create your views here.

def hello(request):
    user = authenticate(username='person', password='ILK123456')

    
    if user is not None:
    # A backend authenticated the credentials
        print(user.get_all_permissions())
        auth_login(request, user)
    else:
        pass
    return HttpResponse("zqq")

@csrf_exempt
def login(request):

    res_dic = json.loads(request.body.decode('utf-8'))
    print(res_dic)

    user = authenticate(username=res_dic['userName'], password=res_dic['passWord'])
    if user is not None:
        auth_login(request, user) # 已经登录，重新登录，或更新过期时间，sessionid不变
        request.session['username'] = user.username # session这时候可以存了
        res = {'res_code': 111, 'res_msg': 'login_success', 'res_data': user.username}

    else:
        res = {'res_code': 112, 'res_msg': 'login_failed', 'res_data': ''}

    return JsonResponse(res)

@csrf_exempt
def logout(request):
    if request.user.is_authenticated:
        res = {'res_code': 113, 'res_msg': 'logout_success', 'res_data': request.session['username']}
        auth_logout(request)
        
    else:
        res = {'res_code': 114, 'res_msg': 'logout_failed', 'res_data': ''}

    return JsonResponse(res)

@ensure_csrf_cookie
def csrf(request):
     return HttpResponse('Hello world')

@csrf_exempt
@login_required
def commit_app(request):
    print('Log: commit application, start...')
    if request.method == 'POST':
        try:
            # 查找当前登录用户姓名
            loginedUserId = request.session.get('_auth_user_id')
            usernameUser = User.objects.get(id=loginedUserId)
            print('Logined user: ', usernameUser, ', type', type(usernameUser))
            # 获取申请表中的信息
            content_result = request.POST.get('content')
            print('Get form data success')

            #添加申请记录的基本信息
            app_record = ApplicationRecord.objects.create(seller=usernameUser,
            updater=usernameUser.username,
            recorder=usernameUser.username,
            lastUpdate=datetime.now())
            print('Model: ApplicationRecord save success, id: ', app_record.id)

            #查找信息并提交
            json_request_data = request.body
            content = json.loads(json_request_data)
            content_data = content.get('content')
            for i in content_data:
                print('content type: ', i.get('type'))
                if i.get('type') == 'renter':
                    renter_info = i.get('data')
                    renter = Renter.objects.create(ar=app_record,
                                    userNameWrite=renter_info.get('UserNameWrite'),
                                    userNameAlias=renter_info.get('UserNameAlias'),
                                    userNameRead=renter_info.get('UserNameRead'),
                                    userAddr=renter_info.get('UserAddr'),
                                    userAddrPostcode=renter_info.get('UserAddrPostCode'),
                                    userPhone=renter_info.get('UserPhone'))
                    print('Model: Renter save success, id: ', renter.ar_id)
                elif i.get('type') == 'manager':
                    company_info = i.get('data')
                    company = Company.objects.create(ar=app_record,
                                    managerCompanyName=company_info.get('ManagerCompanyName'),
                                    managerCompanyAddr=company_info.get('ManagerCompanyAddr'),
                                    managerCompanyChargerName=company_info.get('ManagerCompanyChargerName'),
                                    managerCompanyPhone=company_info.get('ManagerCompanyPhone'))
                    print('Model: Manager save success, id: ', company.ar_id)
                elif i.get('type') == 'thing':
                    thing_info = i.get('data')
                    thing = House.objects.create(ar=app_record,
                                    thingName=thing_info.get('ThingName'),
                                    thingNumber=thing_info.get('ThingNumber'),
                                    structI=thing_info.get('ThingStructI'),
                                    structII=thing_info.get('ThingStructII'),
                                    thingArea=int(thing_info.get('ThingArea')),
                                    stayPeopleNumber=int(thing_info.get('ThingStayPeopleNumber')),
                                    thingAddr=thing_info.get('ThingAddr'),
                                    thingAddrPostcode=thing_info.get('ThingAddrPostcode'),
                                    thingRentCost=thing_info.get('ThingRentCost'),
                                    thingManageCost=thing_info.get('ThingManageCost'),
                                    thingGiftCost=thing_info.get('ThingGiftCost'),
                                    thingDepositCost=thing_info.get('ThingDepositCost'),
                                    thingReliefCost=thing_info.get('ThingReliefCost'))
                    print('Model: Thing save success, id: ', thing.ar_id)
                elif i.get('type') == 'settle':
                    settle_info = i.get('data')
                    settlementDate_format = datetime.strptime(settle_info.get('SettlementDate'), "%Y-%m-%d %H:%M:%S")
                    contractDate_format = datetime.strptime(settle_info.get('ContractDate'), "%Y-%m-%d %H:%M:%S")
                    settle = Live.objects.create(ar=app_record)
                                    # settlementDate=settlementDate_format,
                                    # contractDate=contractDate_format)
                    print('Model: Settle save success, id: ', settle.ar_id)
                elif i.get('type') == 'reward':
                    reward_info = i.get('data')
                    reward = Reward.objects.create(ar=app_record,
                                    AD=reward_info.get('AD'),
                                    agencyFee=reward_info.get('AgencyFee'),
                                    backFee=reward_info.get('BackFee'))
                    print('Model: Reward save success, id: ', reward.ar_id)
                elif i.get('type') == 'tip':
                    tip_info = i.get('data')
                    tip = Tip.objects.create(ar=app_record,
                                tip=tip_info.get('tip'))
                    print('Model: Tip save success, id: ', tip.ar_id)

        except Exception as e:
            print('Log: commit application, error: ', repr(e))
            res = {'res_code': 312, 'res_msg': 'commint_app_resp', 'res_data': repr(e)}
        finally:
            res = {'res_code': 312, 'res_msg': 'commint_app_resp', 'res_data': 'Commit Success'}
            print('Log: commit application, end.')
            return JsonResponse(res)
    else:
        res = {'res_code': 312, 'res_msg': 'commint_app_resp', 'res_data': 'Needing login'}
        return JsonResponse(res)

@csrf_exempt
@login_required
def commit_comment_msg(request):
    # 查找当前登录用户姓名
    if request.method == 'POST':
        print('Log: commit application, start...')
        loginedUserId = request.session.get('_auth_user_id')
        usernameUser = User.objects.get(id=loginedUserId)
        print('Logined user: ', usernameUser, ', type', type(usernameUser))

        content_result = request.POST
        content = json.loads(content_result)
        print('Load data from json, content: ', content)




@csrf_exempt
@login_required
def commit_test(request):
    if request.method == 'POST':
        # loginedUserId = request.session.get('_auth_user_id')
        # usernameUser = User.objects.get(id=loginedUserId)
        # print('Logined user: ', usernameUser)
        # app_record = ApplicationRecord.objects.create(seller=usernameUser,
        #                                               updater=usernameUser.username,
        #                                               recorder=usernameUser.username,
        #                                               lastUpdate=datetime.now())
        # json_content = request.POST.get('content')
        json_content = request.body
        content = json.loads(json_content)
        content_result = content.get('content')
        for i in content_result:
            print(i)
        res = {'msg': 'success'}

        return JsonResponse(res)
