from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    #配置users信息操作路由
    path('users', views.indexUsers,name="indexusers"),
    path('users/add', views.addUsers,name="addusers"),
    path('users/insert', views.insertUsers,name="insertusers"),
    path('users/del/<int:uid>', views.delUsers,name="delusers"),
    path('users/edit/<int:uid>', views.editUsers,name="editusers"),
    path('users/update', views.updateUsers,name="updateusers"),
    
]