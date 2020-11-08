from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from random import *
from sendEmail.views import *
from rest_framework import generics
from .serializers import UserSerializer
import hashlib

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

def index(request):
    return HttpResponseRedirect(reverse('main_index'))

def signin(request):
    return render(request,'member/signin.html')

def login(request):
    loginID=request.POST['user_id']
    loginPW=request.POST['user_password']
    try:
        user=User.objects.get(user_id=loginID)
    except:
        return redirect('member_loginFail')
    encoded_loginPW=loginPW.encode()
    encrypted_loginPW=hashlib.sha256(encoded_loginPW).hexdigest()
    if user.user_password==encrypted_loginPW:
        request.session['user_name']=user.user_name
        request.session['user_id']=user.user_id
        return redirect('main_index')
    else:
        return redirect('member_loginFail')

def loginFail(request):
    return render(request,'member/loginFail.html')
    
def logout(request):
    del request.session['user_name']
    del request.session['user_id']
    return redirect('main_index')

def signup(request):
    return render(request,'member/signup.html')

def join(request):
    name=request.POST['signupName']
    member_id=request.POST['signupID']
    member_email=request.POST['signupEmail']
    member_pw=request.POST['signupPW']
    phone_number=request.POST['signupPhone']
    encoded_pw=member_pw.encode()
    encrypted_pw=hashlib.sha256(encoded_pw).hexdigest()
    user=User(user_name=name,user_id=member_id,user_email=member_email,user_password=encrypted_pw,user_phonenumber=phone_number)
    user.save()
    code=randint(1000,9999)
    response=redirect('member_verifyCode')
    response.set_cookie('code',code)
    response.set_cookie('user_id',user.getid())
    send_result=send(member_email,code)
    if send_result:
        return response
    else:
        return HttpResponse("이메일 발송에 실패했습니다.")

def verifyCode(request):
    return render(request,'member/verifyCode.html')

def verify(request):
    user_code=request.POST['verifyCode']
    cookie_code=request.COOKIES.get('code')
    if user_code==cookie_code:
        user=User.objects.get(user_id=request.COOKIES.get('user_id'))
        user.user_validate=True
        user.save()
        response=redirect('main_index')
        response.delete_cookie('code')
        response.delete_cookie('user_id')
        request.session['user_name']=user.user_name
        request.session['user_id']=user.user_id
        return response
    else:
        redirect('member_verifyCode')