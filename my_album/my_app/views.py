from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#网站首页
def index(request):
    return render(request,"myapp/index.html")
#浏览相册信息
def lookup(request):
    return render(request,"myapp/users/lookup.html")
#发布相册信息
def publish(request):
    pass
#删除相册信息
def delete(request):
    pass
#修改相册信息
def modify(request):
    pass

