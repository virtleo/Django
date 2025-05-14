#coding:utf-8
from django.urls import path,re_path
from django.views.static import serve
from .controller import handler
import os

ueditor_path = os.path.join(os.path.dirname(__file__), "UE")

urlpatterns = [
    path('', handler),
    #path('UE/<str:path>', serve, {'document_root': ueditor_path}),
    re_path( r'^UE/(?P<path>.*)$', serve, {'document_root': ueditor_path})
]
