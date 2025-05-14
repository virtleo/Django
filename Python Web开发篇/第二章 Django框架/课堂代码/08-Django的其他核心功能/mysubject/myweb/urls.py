from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('showstatic', views.showStatic,name="showstatic"), #静态资源加载的案例

    #套静态模板案例
    path('diancan/dcsy', views.dcsy,name="dcsy"), #点餐首页
    path('diancan/dclb', views.dclb,name="dclb"), #点餐列表

    #回话跟踪实例
    path('login', views.login,name="login"), #加载登录表单
    path('doLogin', views.doLogin,name="dologin"), #执行登录操作
    path('doLogOut', views.doLogout,name="dologout"), #执行会员退出操作
]
