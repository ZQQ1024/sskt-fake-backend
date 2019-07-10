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
    permission_add_group

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('hello/', hello),
    path('csrf/', csrf),
    path('commit_test/', commit_test),
    path('commit_app/', commit_app),
    path('commit_comment_test/', commit_comment_test),
    path('commit_comment_msg/', commit_comment_msg),
    path('applications_info/', applications_info),
    path('comment_info/', comment),
    path('applications_info_detail/', app_info_detail),
    path('commit_app_apploadfile/', commit_app_uploadfile),
    path('doc/', doc),
    path('quick_sort/', quick_sort_test),
    path('maincontent_info/', maincontent_info),
    path('confirm_comment/', confirm_comment),
    path('permission_add_admin/', permission_add_admin),
    path('logined_status/', login_status),
    path('permission_add_group/', permission_add_group),
]
