from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from myapp.models import Users

from PIL import Image
import time,os

#网站首页
def index(request):
    return render(request,"myapp/index.html")

#加载文件上传表单
def upload(request):
    return render(request,"myapp/upload.html")
#执行文件上传处理
def doupload(request):
    myfile = request.FILES.get("pic",None)
    if not myfile:
        return HttpResponse("没有上传的文件信息")
    #生成上传后的文件名
    filename = str(time.time())+"."+myfile.name.split('.').pop()
    destination = open("./static/pics/"+filename,"wb+")
    for chunk in myfile.chunks(): #分块读取上传文件内容并写入目标文件
        destination.write(chunk)
    destination.close()

     # 执行图片缩放
    im = Image.open("./static/pics/"+filename)
    # 缩放到75*75(缩放后的宽高比例不变):
    im.thumbnail((75, 75))
    # 把缩放后的图像用jpeg格式保存: 
    im.save("./static/pics/s_"+filename,None)

    return HttpResponse("上传的文件："+filename)


#浏览用户信息
def indexUsers(request):
    try:
        #s = Users.objects.get(id=1)
        #return HttpResponse(s)
        ## 执行数据查询，并放置到模板中
        list = Users.objects.all()
        context = {"userslist":list}
        return render(request,"myapp/users/index.html",context)
    except:
        return HttpResponse("没有找到对应的信息！")

#分页浏览用户信息
def pageUsers(request,pIndex=1):
    try:
        ## 执行数据查询，并放置到模板中
        
        #判断搜索条件并封装
        kw = request.GET.get("keyword",None)
        mywhere = "" #定义一个用于存储搜索条件的变量
        if kw is not None:
            list = Users.objects.filter(name__contains=kw) #对name字段做包含式查询
            mywhere = "?keyword=%s"%(kw) #追加搜索条件
        else:
            list = Users.objects.filter()

        p = Paginator(list,5) #以5条数据一页实例化分页对象
        #判断页码值是否有效(防止越界)
        if pIndex<1:
            pIndex = 1
        if pIndex > p.num_pages:
            pIndex = p.num_pages

        ulist = p.page(pIndex)
        context = {"userslist":ulist,"pIndex":pIndex,"pagelist":p.page_range,"mywhere":mywhere}
        return render(request,"myapp/users/index2.html",context)
    except:
        return HttpResponse("没有找到对应的信息！")


#加载添加用户信息表单
def addUsers(request):  
    return render(request,"myapp/users/add.html")

#执行用户信息添加
def insertUsers(request): 
    try:
        ob = Users()
        #从请求post中获取表单提交的信息，并封装到users的model中
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save() #执行保存
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}
    return render(request,"myapp/users/info.html",context)

#执行用户信息删除操作
def delUsers(request,uid):
    try:
        ob = Users.objects.get(pk=uid) #获取要删除用户信息
        ob.delete() #执行删除
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myapp/users/info.html",context)

#加载修改表单，准备用户信息修改
def editUsers(request,uid):
    try:
        ob = Users.objects.get(pk=uid) #获取要修改的用户信息
        context = {'user':ob}
        return render(request,"myapp/users/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
        return render(request,"myapp/users/info.html",context)

# 执行信息编辑操作
def updateUsers(request):
    try:
        ob = Users.objects.get(id= request.POST['id'])
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        #ob.addtime = datetime.now
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myapp/users/info.html",context)


#富文本编辑器的使用
def myueditor(request):
    return render(request,"myapp/ueditor.html")