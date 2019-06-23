from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

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