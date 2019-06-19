from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from hashlib import sha1

# Create your views here.
from df_user.models import *


def register(request):
    return render(request, 'df_user/register.html')

def register_handle(request):
    # 接收用户参数
    post = request.POST
    user_name = post.get('user_name')
    password = post.get('pwd')
    password2 = post.get('cpwd')
    email = post.get('email')
    # 对照两次密码是否相同
    if password != password2:
        return render(request, 'df_user/register.html')
    # 加密密码
    s1 = sha1()
    s1.update(password.encode('utf8'))
    password3 = s1.hexdigest()
    # 创建对象，保存数据到数据库中
    user = UserInfo()
    user.user_name = user_name
    user.password = password3
    user.email = email
    user.save()

    # 注册成功, 转到登录页面
    return redirect('/login/')

def register_exist(request):    #判断用户名是否已经存在
    user_name = request.GET.get('user_name')
    count = UserInfo.objects.filter(user_name=user_name).count()    #count为0或1
    return JsonResponse({'count':count})

def login(request):
    '''
    登录
    :param request:
    :return:
    '''
    user_name = request.COOKIES.get('user_name', '')
    context = {'title':'用户登录', 'error_name':0, 'error_pwd':0, 'uname': user_name}
    return render(request, 'df_user/login.html', context)

def login_handle(request):
    post = request.POST
    user_name = post.get('username')
    password = post.get('password')
    remeber = post.get('remeber', 0)

    users = UserInfo.objects.filter(user_name=user_name)

    if len(users) == 1:
        s1 = sha1()
        s1.update(password.encode('utf-8'))
        if s1.hexdigest() == users[0].password:
            url = request.COOKIES.get('url', 'df_user/login')
            red = HttpResponseRedirect(url)
            if remeber != 0:
                red.set_cookie('username', user_name)
            else:
                red.set_cookie('username', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['username'] = user_name
            return red
        else:
            context = {'title':'用户登录', 'error_name':0, 'error_pwd':1, 'username':user_name, 'pwd':password}
            return render(request, 'df_user/login.html', context)
    context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'username': user_name, 'upwd': password}
    return render(request, 'df_user/index.html', context)

