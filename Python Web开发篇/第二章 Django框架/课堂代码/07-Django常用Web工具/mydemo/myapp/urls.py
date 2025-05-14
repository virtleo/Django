#当前myapp应用的子路由配置
from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"), #首页

    #文件上传路由配置
    path("upload",views.upload,name="upload"), #加载文件上传表单页
    path("doupload",views.doupload,name="doupload"), #执行文件上传处理

    #分页浏览用户信息
    path('pageusers/<int:pIndex>', views.pageUsers, name="pageusers"), #分页浏览用户信息

    #富文本编辑器的使用
    path('myueditor', views.myueditor, name="myueditor"),

    #用户信息管理
    path('users', views.indexUsers, name="indexusers"), #浏览用户信息
    path('users/add', views.addUsers, name="addusers"), #加载添加用户信息表单
    path('users/insert', views.insertUsers, name="insertusers"), #执行用户信息添加
    path('users/<int:uid>/del', views.delUsers, name="delusers"), #执行用户信息删除
    path('users/<int:uid>/edit', views.editUsers, name="editusers"), #加载用户信息编辑表单
    path('users/update', views.updateUsers, name="updateusers"), #执行用户信息编辑
]