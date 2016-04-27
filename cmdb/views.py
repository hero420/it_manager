#coding=utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import form
from cmdb import models
from django.shortcuts import redirect

# Create your views here.
def login(request):
    if request.method=='POST':
        check_value=form.User_Login(request.POST)
        if check_value.is_valid():
            login_info=check_value.clean()
            if models.User_Info.objects.filter(user=login_info['username'],password=login_info['password']):
                return redirect('/cmdb/index/')
            else:
                return render(request,'account/login.html',{'check_login':'用户名或密码错误,请重新登陆'})
        else:
            error=check_value=check_value.errors
            print (error)
            return render(request,'account/login.html',{'error':error})

    return render(request,'account/login.html')

def index(request):
    return render(request,'home/index.html')

def check_user(request):
    check_user=request.GET.get('username')
    print (request.GET.get('username'))
    if check_user:
        if not models.User_Info.objects.filter(user=check_user):
            return HttpResponse('false')
        else:
            return HttpResponse('true')
def resource(request):
    return render(request,'resource/index.html')
def test(request):
    return render(request,'test.html')