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
    path('commit_app/', views.commit_app),
    path('commit_comment_test/', views.commit_comment_test),
    path('commit_comment_msg/', views.commit_comment_msg),
    path('applications_info/', views.applications_info),
    path('comment_info/', views.comment),
    path('applications_info_detail/', views.app_info_detail),
    path('commit_app_apploadfile/', views.commit_app_uploadfile),
    path('doc/', views.doc),
    path('quick_sort/', views.quick_sort_test),
    path('maincontent_info/', views.maincontent_info),
    path('confirm_comment/', views.confirm_comment),
    path('permission_add_admin/', views.permission_add_admin),
    path('logined_status/', views.login_status),
    path('permission_add_group/', views.permission_add_group),
    path('permission_add_user_to_group/', views.permission_add_user_to_group),
    path('permission_add_group_leader/', views.permission_addgroup_leader),
    path('index/', views.index),
    path('login_page/', views.login_page),
]
