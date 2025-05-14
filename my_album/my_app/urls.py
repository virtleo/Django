from django.urls import path
from my_app import views
urlpatterns = [
    #path("admin/", admin.site.urls),
    #首页
    path("",views.index,name="index"),
    #浏览相册信息
    path("lookup",views.lookup,name="lookup"),
    
    #发布相册信息
    path("publish",views.publish,name="publish"),
    #删除相册信息
    path("delete",views.delete,name="delete"),
    #修改相册信息
    path("modify",views.modify,name="modify"),
    
]