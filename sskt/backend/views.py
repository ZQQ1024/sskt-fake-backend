from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ApplicationRecord, House, Company, Reward, Live, Tip, Renter, Comment, File, UserGroup, UserAdmin, \
    Group
from django.utils import timezone
from datetime import datetime
from .custom_exception import NullResultQueryException, NoneUploadfileException, UploadfileExistedException,\
    NoMatchingAppException, ConfirmCommentFailException, UserGroupErrorException, GroupErrorException,\
    AddGroupErrorException, NameCollecErrorException
from .tools import cus_quick_sort
import os
import copy
import traceback
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
@login_required
def login_status(request):
    if request.method == 'POST':
        logined_user = User.objects.get(id=request.session.get('_auth_user_id'))
        print('session: ', request.session)
        res = {'username': logined_user.username}
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

def working_flag(string, flag='starting'):
    print('--------', string, ', ', flag, '.--------')

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
                                                    upPerson=app_obj[0].seller.username,
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

def get_name_collec(username_str):
    res_data = []
    working_flag('get_name_collec()', 'start')
    print('name string: ', username_str)
    try:
        user_obj = User.objects.filter(username=username_str)
        # print(len(user_obj))
        if len(user_obj) > 0:
            user_id = user_obj[0].id
            user_admin_obj = UserAdmin.objects.filter(user=user_obj[0])
            if len(user_admin_obj) > 0:
                print('usr is in admin table')
                if user_admin_obj[0].is_admin == 1:
                    print('user is admin')
                    for i in User.objects.all():
                        res_data.append(i.username)
            else:
                print('usr is not in admin table')
                usergroup__obj = UserGroup.objects.filter(user=user_obj[0])
                if len(usergroup__obj) > 0:
                    group_obj = Group.objects.filter(id=usergroup__obj[0].group)
                    if len(group_obj) > 0:
                        print('user is group leader, group: ', group_obj[0].name)
                        if group_obj[0].leader == user_id:
                            user_group_collec_obj = UserGroup.objects.all()
                            for j in user_group_collec_obj:
                                if j.group == group_obj[0].id:
                                    res_data.append(j.user.username)
                        else:
                            # user in user's group, but no leader
                            print('user in user\'s group, but no leader')
                            res_data.append(username_str)
                    else:
                        # usergroup's group not existed
                        print('usergroup\'s group not existed')
                        res_data.append(username_str)
                else:
                    # user's usergroup not existed
                    print('user\'s usergroup not existed')
                    res_data.append(username_str)
    except Exception as e:
        res_data.clear()
        traceback.print_exc()
        print('Loc: get_name_collec()', repr(e))
        working_flag('get_name_collec', 'error')
        return res_data
    else:
        working_flag('get_name_collec', 'end')
        return res_data


@csrf_exempt
@login_required
def applications_info(request):
    working_flag('applications_info()', 'start')
    res_data = []
    try:
        user_id = request.session.get('_auth_user_id')
        user_obj = User.objects.filter(id=user_id)
        # print(user_obj[0].username, ' ', type(user_obj[0].username))
        name_collec = get_name_collec(user_obj[0].username)
        # name_collec = []
        print('Name collection: ', name_collec)

        app_item = {}
        # 基本返回信息
        app_objs = ApplicationRecord.objects.all()
        print('Search app info start: ')
        for i in app_objs:
            if i.seller.username not in name_collec:
                print('Skip, username: ', i.seller.username)
                continue
            print('---------', i, '----------')
            app_item = {}

            user_obj = User.objects.get(id=i.seller.id)
            app_item.setdefault('seller', user_obj.username)
            print('Seller info finished')

            app_item.setdefault('manager_number', i.manager_number)
            app_item.setdefault('recorder', i.recorder)
            app_item.setdefault('status', i.status)
            app_item.setdefault('update_person', i.updater)
            app_item.setdefault('update_time', i.lastUpdate)
            app_item.setdefault('commit_time', i.createDate)
            print('Base info finished')

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
        traceback.print_exc()
        print('Log: show applications, error: ', repr(e))
        res = {'res_code': 311, 'res_msg': 'applications_info', 'res_repr': repr(e), 'res_data': res_data}
        working_flag('applications_info', 'error')
        return JsonResponse(res)
    else:
        working_flag('applications_info', 'end')
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
                res_item.setdefault('Comment_id', i.id)
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
def confirm_comment(request):
    working_flag('confirm_comment', 'start')
    try:
        if request.method == 'POST':
            json_content = request.body
            content = json.loads(json_content)
            comment_id = content.get('Comment_id')
            comment_obj = Comment.objects.filter(id=comment_id)
            if len(comment_obj) > 0:
                if comment_obj[0].status == 'Unchecked':
                    comment_obj.update(status='Checked')
                else:
                    error_str = 'Loc: confirm_comment(), comment status error, comment id: ' + str(comment_id) +\
                                ', status: ' + comment_obj[0].status
                    raise ConfirmCommentFailException(error_str)
            else:
                error_str = 'Loc: confirm_comment(), comment is not exist, comment id: ' + comment_id
                raise ConfirmCommentFailException(error_str)
        else:
            raise ConfirmCommentFailException('Loc: confirm_comment(), submit method is not POST.')
    except Exception as e:
        working_flag('confirm_comment', 'error')
        traceback.print_exc()
        res = {'res_code': 316, 'res_msg': 'confirm failed'}
        return JsonResponse(res)
    else:
        working_flag('confirm_comment', 'end')
        res = {'res_code': 316, 'res_msg': 'confirm successed'}
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

@csrf_exempt
@login_required
def commit_app_uploadfile(request):
    print('--------Upload file, start.--------')
    try:
        if request.method == 'POST':
            # 查询关联的申请记录
            sskt_num = request.POST.get('sskt_num')
            app_obj = ApplicationRecord.objects.filter(manager_number=sskt_num)
            if len(app_obj) != 0:
                app_id = app_obj[0].id
            else:
                app_id = -1
            if app_id == -1:
                print('null result searching for application')
                raise NullResultQueryException('Loc: commit_app_uploadfile(), searching for'
                                               ' application failed')

            # 上传文件存储位置，不存在则新建
            up_path = './uploadfile'
            filename = request.POST.get('file_name')
            up_path = up_path + '/' + app_obj[0].manager_number
            print('upload file absolute path: ', os.path.abspath(up_path))
            folder = os.path.exists(up_path)
            if not folder:
                print('make dir: ', up_path)
                os.makedirs(up_path)

            up_name = up_path + '/' + filename
            # 文件查重
            file_sear_obj = File.objects.filter(path=up_name)
            if len(file_sear_obj) != 0:
                print('uploadfile_fail, file exist')
                raise UploadfileExistedException('Loc: commit_app_uploadfile(), upload file existed.')

            file_obj = File.objects.create(ar=app_obj[0],
                                           path=up_name)
            print('Model: File save success. file id: ', file_obj.id)

            file_data = request.FILES.get('upload_file', None)
            if not file_data:
                print('None upload file')
                raise NoneUploadfileException('Loc: commit_app_uploadfile()')
            with open(up_name, 'wb') as f:
                for chunk in file_data.chunks():
                    f.write(chunk)
                print('Upload file over')

    except Exception as e:
        print('Log: upload file fail, error: ', str(e))
        res = {'res_code': 3152, 'res_msg': 'uploadfile fail', 'res_repr': str(e)}
        print('--------Upload file error, end.--------')
        return JsonResponse(res)
    else:
        res = {'res_code': 3151, 'res_msg': 'uploadfile succ'}
        print('--------Upload file, end.--------')
        return JsonResponse(res)


@csrf_exempt
@login_required
def doc(request):
    print('--------Doc, start--------')
    try:
        res_data = []
        file_content = {}
        file_obj = File.objects.all()
        print('start making file content dict')
        for i in file_obj:
            # print(i.ar_id, i.path)
            file_value = []
            # first insert value
            file_content.setdefault(i.ar_id, file_value)
            file_content[i.ar_id].append(i.path)
        print('end making file content dict')
        for j in file_content:
            file_temp = {}
            app_obj = ApplicationRecord.objects.filter(id=j)
            if len(app_obj) > 0:
                file_temp['SSKT_number'] = app_obj[0].manager_number
                file_temp['file_string'] = file_content[j]
            else:
                file_temp['SSKT_number'] = 'Unknown'
                file_temp['file_string'] = file_content[j]
                raise NoMatchingAppException('Loc: doc(). ApplicationRecord id: ', i.ar_id)
            res_data.append(file_temp)
    except Exception as e:
        print('Doc error: ', repr(e))
        print('--------Doc error.--------')
    finally:
        print(res_data)
        res = {'content': res_data}
        print('--------Doc, end.--------')
        return JsonResponse(res)

@csrf_exempt
@login_required
def maincontent_info(request):
    working_flag('maincontent_info', 'starting')
    try:
        res_data=[]
        has_name=[]
        rank_temp = {'rank': 0, 'username': 'null', 'money': 0, 'number': 0}
        app_objs = ApplicationRecord.objects.all()
        if len(app_objs) > 0:
            for i in app_objs:
                print('username: ', i.seller.username)
                if i.seller.username in has_name:
                    working_flag('fun!!!', '1')
                    index = has_name.index(i.seller.username)
                    item = res_data[index]
                    item['number'] += 1
                    reward_obj = Reward.objects.filter(ar_id=i.id)
                    if len(reward_obj) > 0:
                        item['money'] += int(reward_obj[0].AD) + int(reward_obj[0].agencyFee) \
                                         - int(reward_obj[0].backFee)
                    else:
                        item['money'] += 0
                else:
                    working_flag('fun!!!', '2')
                    has_name.append(i.seller.username)
                    item = copy.deepcopy(rank_temp)
                    item['username'] = i.seller.username
                    item['number'] += 1
                    reward_obj = Reward.objects.filter(ar_id=i.id)
                    if len(reward_obj) > 0:
                        item['money'] += int(reward_obj[0].AD) + int(reward_obj[0].agencyFee)\
                                         - int(reward_obj[0].backFee)
                    else:
                        item['money'] += 0
                    res_data.append(item)
            print('App count completed.')

            # quick sort for res_data
            cus_quick_sort(res_data, 0, len(res_data)-1)
            rank_index = 1
            for i in res_data:
                i['rank'] = rank_index
                rank_index += 1
            print('Res data sort completed')
        else:
            raise NullResultQueryException('Loc: maincontent_info(), ApplicationRecord '
                                           'has no items')
    except Exception as e:
        res = {'content': []}
        print('Maincontent_info error: ', repr(e))
        working_flag('maincontent_info', 'error')
        return JsonResponse(res)
    else:
        res = {'content': res_data}
        working_flag('maincontent_info', 'end')
        return JsonResponse(res)


def quick_sort_test(request):
    arry = []
    arry.append({'rank': 0, 'username': '1', 'money': 5, 'number': 0})
    arry.append({'rank': 0, 'username': '2', 'money': 1, 'number': 0})
    arry.append({'rank': 0, 'username': '3', 'money': 4, 'number': 0})
    arry.append({'rank': 0, 'username': '4', 'money': 3, 'number': 0})
    arry.append({'rank': 0, 'username': '5', 'money': 8, 'number': 0})

    cus_quick_sort(arry,0,len(arry)-1)
    print(arry)
    return HttpResponse(200)

@csrf_exempt
@login_required
def permission_add_admin(request):
    working_flag('permission_add_admin', 'start')
    try:
        if request.method == 'POST':
            loginedUserId = request.session.get('_auth_user_id')
            usernameUser_obj = User.objects.filter(id=loginedUserId)
            user_group_obj = UserAdmin.objects.filter(user=usernameUser_obj[0])
            if len(user_group_obj) > 0:
                user_group_obj.update(is_admin=1)
            else:
                new_user_group_obj = UserAdmin.objects.create(
                                            user=usernameUser_obj[0],
                                            is_admin=3)
        else:
            raise UserGroupErrorException('Loc: permission_add_admin(), submit method is not POST.')
    except Exception as e:
        res = {'res_code': 512, 'res_msg': 'add admin failed'}
        traceback.print_exc()
        working_flag('permission_add_admin', 'error')
        return JsonResponse(res)
    else:
        res = {'res_code': 512, 'res_msg': 'add admin successed'}
        working_flag('permission_add_admin', 'end')
        return JsonResponse(res)

@csrf_exempt
@login_required
def permission_add_group(request):
    working_flag('permission_add_group', 'start')
    try:
        if request.method == 'POST':
            content = json.loads(request.body)
            group_name = content.get('name')

            group_object = Group.objects.filter(name=group_name)
            if len(group_object) > 0:
                raise GroupErrorException('Loc: permission_add_group(), group is extisted, add failed.')
            else:
                new_group_object = Group.objects.create(name=group_name)
        else:
            raise GroupErrorException('Loc: permission_add_group(), submit method is not POST.')
    except Exception as e:
        res = {'res_code': 511, 'res_msg': 'add group failed'}
        traceback.print_exc()
        working_flag('permission_add_group', 'error')
        return JsonResponse(res)
    else:
        res = {'res_code': 511, 'res_msg': 'add group successed'}
        working_flag('permission_add_group', 'end')
        return JsonResponse(res)

@csrf_exempt
@login_required
def permission_addgroup_leader(request):
    working_flag('permission_addgroup_leader', 'start')
    try:
        if request.method == 'POST':
            content = json.loads(request.body)
            group_name = content.get('name')
            leader_name = content.get('leader')

            user_obj = User.objects.filter(username=leader_name)
            group_object = Group.objects.filter(name=group_name)
            if len(group_object) > 0:
                if len(user_obj) > 0:
                    group_object.update(leader=user_obj[0].id)
            else:
                raise GroupErrorException('Loc: permission_addgroup_leader(), group not existed.')
                # new_group_object = Group.objects.create(name=group_name)
        else:
            raise GroupErrorException('Loc: permission_addgroup_leader(), submit method is not POST.')
    except Exception as e:
        res = {'res_code': 514, 'res_msg': 'add group leader failed'}
        traceback.print_exc()
        working_flag('permission_addgroup_leader', 'error')
        return JsonResponse(res)
    else:
        res = {'res_code': 511, 'res_msg': 'add group leader successed'}
        working_flag('permission_addgroup_leader', 'end')
        return JsonResponse(res)

@csrf_exempt
@login_required
def permission_add_user_to_group(request):
    working_flag('permission_add_user_to_group', 'start')
    try:
        if request.method == 'POST':
            loginedUserId = request.session.get('_auth_user_id')
            usernameUser_obj = User.objects.filter(id=loginedUserId)

            content = json.loads(request.body)
            group_name = content.get('group_name')
            group_obj = Group.objects.filter(name=group_name)
            if len(group_obj) > 0:
                group_id = group_obj[0].id
            else:
                raise AddGroupErrorException('Loc: permission_add_user_to_group(), group not existed.')

            user_group_obj = UserGroup.objects.filter(user=usernameUser_obj[0])
            if len(user_group_obj) > 0:
                user_group_obj.update(group=group_id)
            else:
                new_user_group = UserGroup.objects.create(user=usernameUser_obj[0],
                                                          group=group_id)
        else:
            raise AddGroupErrorException('Loc: permission_add_user_to_group(), submit method is not POST.')
    except Exception as e:
        res = {'res_code': 513, 'res_msg': 'add user to group failed'}
        traceback.print_exc()
        working_flag('permission_add_user_to_group', 'error')
        return JsonResponse(res)
    else:
        res = {'res_code': 513, 'res_msg': 'add user to group successed'}
        working_flag('permission_add_user_to_group', 'end')
        return JsonResponse(res)