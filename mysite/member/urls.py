from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view
from . import views
from .views import *

urlpatterns=[
    path('',views.index,name='member_index'),
    path('signup',views.signup,name='member_signup'),
    path('signup/join',views.join,name='member_join'),
    path('signin',views.signin,name='member_signin'),
    path('signin/login',views.login,name='member_login'),
    path('loginFail',views.loginFail,name='member_loginFail'),
    path('logout',views.logout,name='member_logout'),
    path('verifyCode',views.verifyCode,name='member_verifyCode'),
    path('verify',views.verify,name='member_verify'),
    path('api/',UserList.as_view(),name='member_api'),
    path('api/<int:pk>/',UserDetail.as_view(),name='member_api_detail'),
    path('api/doc/',get_swagger_view(title="User API Manuaal")),
]