"""sskt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend.views import hello, csrf, login, logout, commit_test,\
    commit_app, commit_comment_test, commit_comment_msg, applications_info,\
    comment, app_info_detail, commit_app_uploadfile, doc, quick_sort_test,\
    maincontent_info, confirm_comment, login_status, permission_add_admin,\
    permission_add_group,permission_add_user_to_group, permission_addgroup_leader
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('logout/', views.logout),
    path('hello/', views.hello),
    path('csrf/', views.csrf),
    path('commit_test/', views.commit_test),
    path('commit_app/', views.commit_app),  # 提交申请
    path('commit_comment_test/', views.commit_comment_test),
    path('commit_comment_msg/', views.commit_comment_msg),  # 提交留言
    path('applications_info/', views.applications_info),    # 显示申请信息，即申入一览
    path('comment_info/', views.comment),   #显示留言
    path('applications_info_detail/', views.app_info_detail),   # 显示申请细节
    # path('commit_app_apploadfile/', views.commit_app_uploadfile),
    path('doc/', views.doc),    # 显示上传文件
    path('quick_sort/', views.quick_sort_test),
    path('maincontent_info/', views.maincontent_info),  # 卖上排名，即揭示板
    path('confirm_comment/', views.confirm_comment),    # 确认留言
    path('permission_add_admin/', views.permission_add_admin),      # 添加管理员权限
    path('logined_status/', views.login_status),    # 当前登陆用户
    path('permission_add_group/', views.permission_add_group),      # 添加权限组
    path('permission_add_user_to_group/', views.permission_add_user_to_group),      # 权限组添加用户
    path('permission_add_group_leader/', views.permission_addgroup_leader),     # 权限组添加组长
    path('index/', views.index),    # index页面
    path('login_page/', views.login_page),      # 登录页面
    path('app_info_update/', views.update_app),     # 修改申请信息细节
]
