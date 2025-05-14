from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# 网站首页的访问入口方法
def index(request):
    #return HttpResponse("ok!")
    return render(request,"index.html")

#加载静态内容实例
def showStatic(request):
    return render(request,"mystatic.html")

#加载登录表单页
def login(request):
    return render(request,"login.html")

#加载登录表单页
@csrf_exempt
def doLogin(request):
    #验证登录账号和密码
    uname = request.POST.get("username",None)
    upass = request.POST.get("password",None)
    if uname=="zhangsan" and upass=='123':
        #登录成功,将当前地登录成功的会员信息放置到session中
        request.session['diancan_user'] = {'username':uname,'password':upass}
        return redirect(reverse('index'))
    else:
        #登录失败
        context = {'errorinfo':"登录账号或密码错误！"}
        return render(request,"login.html",context)

#执行会员退出
def doLogout(request):
    del request.session['diancan_user'] #删除session信息
    return redirect(reverse('login'))


#点餐首页
def dcsy(request):
    #导入model，并从数据库中获取当前店铺下所有的菜品信息，并放置到下面模板中
    return render(request,"diancan/dcsy.html")

#点餐列表
def dclb(request):
    return render(request,"diancan/dclb.html")