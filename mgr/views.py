from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from mgr import models
from django.conf import settings

sip = settings.ALLOWED_HOSTS[0]

import json
def login(request):
    global sip
    host = request.get_host().split(":")
    sip = host[0]
    print(sip)
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')

def uselogin(request):
    if request.method == "POST":
       action = request.POST
       login1 = "用户名输入错误，用户不存在！"
       login2 = "密码输入错误！"
       login3 = "请选择正确的用户类型！"
       # print(verify)
       try:
           # 根据 id 从数据库中找到相应的客户记录
           verify = models.PhcUser.objects.get(username=action['usename'])
           if verify.password == action['password']:
               if verify.action == int(action['usertype']):
                   request.session['ip'] = "19216801"
                   request.session['username'] = verify.username
                   return render(request, 'index.html',{'username':verify.username, 'ip':sip, 'roomnum':'19216801'})
               else:
                   return render(request, 'login.html', {'erro3': login3})
           else:
               return render(request, 'login.html', {'erro2': login2})
       except models.PhcUser.DoesNotExist:
           return render(request, 'login.html', {'erro1':login1})
    else:
       return HttpResponse("登录失败")

def useregister(request):
    if request.method == "POST":
       action = request.POST
       register1 = "用户名不能为空!"
       register2 = "密码不能为空!"
       register3 = "两次密码输入不一致!"
       if action['usename']:
           if action['password1']:
               if action['password1']==action['password2']:
                   models.PhcUser.objects.create(username=action['usename'],password=action['password2'],action=0)
                   return render(request, 'registersuccess.html')
               else:
                   return render(request, 'register.html', {'erro3': register3})
           else:
               return render(request, 'register.html', {'erro2':register2})
       else:
           return render(request, 'register.html', {'erro1':register1})
    else:
       return HttpResponse("注册失败")

def get_username():
    return USERNAME

