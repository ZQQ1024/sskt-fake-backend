from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ApplicationRecord, House, Company, Reward, Live, Tip, Renter, Comment
from django.utils import timezone
from datetime import datetime
from .custom_exception import NullResultQueryException

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
            lastUpdate=timezone.now())
            print('Model: ApplicationRecord save success, id: ', app_record.id)
            ApplicationRecord.objects.filter(id=app_record.id).update(manager_number='-'.join(['sskt', str(app_record.id)]))

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
                    settle = Live.objects.create(ar=app_record,
                                     settlementDate=settlementDate_format,
                                     contractDate=contractDate_format)
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
            res = {'res_code': 312, 'res_msg': 'commit_app_resp', 'res_data': 'Commit Success'}
            print('Log: commit application, end.')
        except Exception as e:
            print('Log: commit application, error: ', repr(e))
            res = {'res_code': 312, 'res_msg': 'commit_app_resp', 'res_data': repr(e)}
        finally:
            return JsonResponse(res)
    else:
        res = {'res_code': 312, 'res_msg': 'commit_app_resp', 'res_data': 'Needing login'}
        return JsonResponse(res)

@csrf_exempt
@login_required
def commit_comment_msg(request):
    try:
        if request.method == 'POST':
            print('Log: commit application, start...')
            # 查找当前登录用户姓名
            loginedUserId = request.session.get('_auth_user_id')
            usernameUser = User.objects.get(id=loginedUserId)
            print('Logined user: ', usernameUser, ', type', type(usernameUser))

            content_result = request.body
            content = json.loads(content_result)
            print('Load data from json, content: ', content)
            sskt_num = content.get('sskt_num')
            comment_content = content.get('Content')
            app_obj = ApplicationRecord.objects.filter(manager_number=sskt_num)
            if len(app_obj) != 0:
                comment_obj = Comment.objects.create(ar=app_obj[0],
                                                    upPerson=usernameUser.username,
                                                    createPerson=usernameUser.username,
                                                    updatePerson=usernameUser.username,
                                                    content=comment_content)
                print('Model: Comment save success, id: ', comment_obj.ar_id)
                res = {'res_code': 314, 'res_msg': 'commit_comment_resp', 'res_data': 'Commit Success'}
            else:
                print('Model: Comment save failed, Application info not exist, sskt: ', sskt_num)
        else:
            res = {'res_code': 314, 'res_msg': 'commit_comment_resp', 'res_data': 'Needing login'}
    except Exception as e:
        print('Log: commit comment, error: ', repr(e))
        res = {'res_code': 314, 'res_msg': 'commit_comment_resp', 'res_data': repr(e)}
    finally:
        return JsonResponse(res)

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
        json_content = request.POST.get('content')
        content = json.loads(json_content)
        for i in content:
            print(i)
        res = {'msg': 'success'}

        return JsonResponse(res)

@csrf_exempt
@login_required
def commit_comment_test(request):
    if request.method == 'POST':
        json_content = request.body
        content = json.loads(json_content)
        app_id_result = content.get('App_id')
        content_result = content.get('Content')

        print('app id: ', app_id_result)
        print('content: ', content_result)
        res = {'msg': 'success'}
        return JsonResponse(res)

@csrf_exempt
@login_required
def applications_info(request):
    try:
        app_item = {}
        res_data = []
        # 基本返回信息
        app_objs = ApplicationRecord.objects.all()
        # print('Search application result: ', app_objs)
        for i in app_objs:
            print('---------', i, '----------')
            app_item = {}
            app_item.setdefault('manager_number', i.manager_number)
            app_item.setdefault('recorder', i.recorder)
            app_item.setdefault('status', i.status)
            app_item.setdefault('update_person', i.updater)
            app_item.setdefault('update_time', i.lastUpdate)
            app_item.setdefault('commit_time', i.createDate)
            print('Base info finished')

            user_obj = User.objects.get(id=i.seller.id)
            app_item.setdefault('seller', user_obj.username)
            print('Seller info finished')

            manager_obj = Company.objects.filter(ar_id=i.id)
            if len(manager_obj) != 0:
                app_item.setdefault('manager_name', manager_obj[0].managerCompanyName)
                app_item.setdefault('manager_phone', manager_obj[0].managerCompanyPhone)
            else:
                app_item.setdefault('manager_name', 'None')
                app_item.setdefault('manager_phone', 'None')
            print('Company info finished')

            house_obj = House.objects.filter(ar_id=i.id)
            if len(house_obj) != 0:
                app_item.setdefault('item_name', house_obj[0].thingName)
                app_item.setdefault('item_number', house_obj[0].thingNumber)
            else:
                app_item.setdefault('item_name', 'None')
                app_item.setdefault('item_number', 'None')
            print('Thing info finished')
            # 标红状态
            comment_objs = Comment.objects.filter(ar_id=i.id)
            spe_flag = 1
            if len(comment_objs) != 0:
                for j in comment_objs:
                    if j.status == 'unchecked':
                        spe_flag = 0
                        break
                if spe_flag == 0:
                    app_item.setdefault('specify_flag', 'RED')
                elif spe_flag == 1:
                    app_item.setdefault('specify_flag', 'NORMAL')
            else:
                app_item.setdefault('specify_flag', 'NORMAL')
            print('Specify_flag info finished')
            print('-----------------------------------------------')
            res_data.append(app_item)

    except Exception as e:
        print('Log: show applications, error: ', repr(e))
        res = {'res_code': 311, 'res_msg': 'applications_info', 'res_repr': repr(e), 'res_data': res_data}
        return JsonResponse(res)
    finally:
        res = {'apps_info': res_data}
        return JsonResponse(res)

@csrf_exempt
@login_required
def comment(request):
    try:
        res_item = {}
        res_data = []
        sskt_num = request.GET.get('sskt_num')
        app_res = ApplicationRecord.objects.filter(manager_number=sskt_num)
        if len(app_res) != 0:
            comment_res = Comment.objects.filter(ar_id=app_res[0].id)
        else:
            comment_res = None

        if comment_res is None or len(comment_res) == 0:
            raise NullResultQueryException('Loc: comment(), comment result not exist')
        else:
            for i in comment_res:
                res_item = {}
                res_item.setdefault('CreatePerson', i.createPerson)
                res_item.setdefault('CreateDate', i.createDate)
                res_item.setdefault('UpdatePerson', i.updatePerson)
                res_item.setdefault('UpdateDate', i.updateDate)
                res_item.setdefault('Status', i.status)
                res_item.setdefault('Content', i.content)
                res_data.append(res_item)

    except Exception as e:
        print('Log: show comment, error: ', repr(e))
        res = {'res_code': 313, 'res_msg': 'comment_resp', 'res_repr': repr(e), 'res_data': res_data}
        return JsonResponse(res)
    # except NullResultQueryException as nullresult_e:
    #     print('Log: show comment, error: ', repr(nullresult_e))
    #     res = {'res_code': 313, 'res_msg': 'comment_resp', 'res_repr': repr(nullresult_e), 'res_data': res_data}
    #     return JsonResponse(res)
    finally:
        res = {'comments_info': res_data}
        return JsonResponse(res)

@csrf_exempt
@login_required
def app_info_detail(request):
    print('--------Searching app info detail, start.--------')
    try:
        res_data = []
        sskt_num = request.GET.get('sskt_num')
        app_res = ApplicationRecord.objects.filter(manager_number=sskt_num)
        if len(app_res) != 0:
            app_id = app_res[0].id
        else:
            app_id = None

        if app_id is None:
            raise NullResultQueryException('Loc: app_info_detail(), application info detail'
                                           ' result not exist')
        else:
            # 添加SSKT番号
            sskt_data = {'type': 'sskt_num',
                        'data': {
                            'sskt_num': sskt_num
                        }}
            res_data.append(sskt_data)
            print('sskt num info completed')
            # 查询租户信息
            renter_obj = Renter.objects.filter(ar_id=app_id)
            if len(renter_obj) != 0:
                renter_data = {'type': 'renter',
                               'data': {
                                   'UserNameWrite': renter_obj[0].userNameWrite,
                                   'UserNameAlias': renter_obj[0].userNameAlias,
                                   'UserNameRead': renter_obj[0].userNameRead,
                                   'UserAddr': renter_obj[0].userAddr,
                                   'UserAddrPostCode': renter_obj[0].userAddrPostcode,
                                   'UserPhone': renter_obj[0].userPhone
                               }}
            else:
                renter_data = {'type': 'renter',
                               'data': {
                                   'UserNameWrite': 'Null',
                                   'UserNameAlias': 'Null',
                                   'UserNameRead': 'Null',
                                   'UserAddr': 'Null',
                                   'UserAddrPostCode': 'Null',
                                   'UserPhone': 'Null'
                               }}
            res_data.append(renter_data)
            print('renter info completed')
            # 查询管理公司信息
            manager_obj = Company.objects.filter(ar_id=app_id)
            if len(manager_obj) != 0:
                manager_data = {
                    'type': 'manager',
                    'data': {
                        'ManagerCompanyName': manager_obj[0].managerCompanyName,
                        'ManagerCompanyAddr': manager_obj[0].managerCompanyAddr,
                        'ManagerCompanyChargerName': manager_obj[0].managerCompanyChargerName,
                        'ManagerCompanyPhone': manager_obj[0].managerCompanyPhone
                    }}
            else:
                manager_data = {
                    'type': 'manager',
                    'data': {
                        'ManagerCompanyName': 'Null',
                        'ManagerCompanyAddr': 'Null',
                        'ManagerCompanyChargerName': 'Null',
                        'ManagerCompanyPhone': 'Null'
                    }}
            res_data.append(manager_data)
            print('company info completed')
            # 查询物件信息
            thing_obj = House.objects.filter(ar_id=app_id)
            if len(thing_obj) != 0:
                thing_data = {
                    'type': 'thing',
                    'data': {
                        'ThingName': thing_obj[0].thingName,
                        'ThingNumber': thing_obj[0].thingNumber,
                        'ThingStructI': thing_obj[0].structI,
                        'ThingStructII': thing_obj[0].structII,
                        'ThingArea': str(thing_obj[0].thingArea),
                        'ThingStayPeopleNumber': str(thing_obj[0].stayPeopleNumber),
                        'ThingAddr': thing_obj[0].thingAddr,
                        'ThingAddrPostcode': thing_obj[0].thingAddrPostcode,
                        'ThingRentCost': thing_obj[0].thingRentCost,
                        'ThingManageCost': thing_obj[0].thingManageCost,
                        'ThingGiftCost': thing_obj[0].thingGiftCost,
                        'ThingDepositCost': thing_obj[0].thingDepositCost,
                        'ThingReliefCost': thing_obj[0].thingReliefCost
                    }}
            else:
                thing_data = {
                    'type': 'thing',
                    'data': {
                        'ThingName': 'Null',
                        'ThingNumber': 'Null',
                        'ThingStructI': 'Null',
                        'ThingStructII': 'Null',
                        'ThingArea': 'Null',
                        'ThingStayPeopleNumber': 'Null',
                        'ThingAddr': 'Null',
                        'ThingAddrPostcode': 'Null',
                        'ThingRentCost': 'Null',
                        'ThingManageCost': 'Null',
                        'ThingGiftCost': 'Null',
                        'ThingDepositCost': 'Null',
                        'ThingReliefCost': 'Null',
                    }}
            res_data.append(thing_data)
            print('thing info completed')
            # 查询入住信息
            settle_obj = Live.objects.filter(ar_id=app_id)
            if len(settle_obj) != 0:
                settle_data = {
                    'type': 'settle',
                    'data': {
                        'SettlementDate': datetime.strftime(settle_obj[0].settlementDate, "%Y-%m-%d"),
                        'ContractDate': datetime.strftime(settle_obj[0].contractDate, "%Y-%m-%d")
                }}
            else:
                settle_data = {
                    'type': 'settle',
                    'data': {
                        'SettlementDate': 'Null',
                        'ContractDate': 'Null'
                    }}
            res_data.append(thing_data)
            print('settle info completed')
            # 查询报酬信息
            reward_obj = Reward.objects.filter(ar_id=app_id)
            if len(reward_obj) != 0:
                reward_data = {
                    'type': 'reward',
                    'data': {
                        'AD': reward_obj[0].AD,
                        'AgencyFee': reward_obj[0].agencyFee,
                        'BackFee': reward_obj[0].backFee,
                }}
            else:
                reward_data = {
                    'type': 'reward',
                    'data': {
                        'AD': 'Null',
                        'AgencyFee': 'Null',
                        'BackFee': 'Null'
                    }}
            res_data.append(reward_data)
            print('reward info completed')
            # 查询备注信息
            tip_obj = Tip.objects.filter(ar_id=app_id)
            if len(tip_obj) != 0:
                tip_data = {
                    'type': 'tip',
                    'data': {
                        'tip': tip_obj[0].tip
                }}
            else:
                tip_data = {
                    'type': 'tip',
                    'data': {
                        'tip': 'Null'
                }}
            res_data.append(tip_data)
            print('tip info completed')

    except Exception as e:
        print('Log: show app info, error: ', repr(e))
        res = {'res_code': 3121, 'res_msg': 'resp_app_info_deatail', 'res_repr': repr(e), 'res_data': res_data}
        print('--------Searching app info detail, end.--------')
        return JsonResponse(res)
    finally:
        res = {'content': res_data}
        print('--------Searching app info detail, end.--------')
        return JsonResponse(res)
