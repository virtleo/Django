from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Stu
# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def add(request):
    lists = Stu.objects.all()
    for stu in lists:
        print(stu)
    
    print(Stu.objects.get(id=6))
    return HttpResponse("Add.....")

