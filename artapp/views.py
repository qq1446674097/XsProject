from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    # 请求路径和请求方法
    print(request.path, request.method, request.META)
    # 请求头的源信息和GET请求参数（查询参数）
    print(request.META)
    print(request.GET)
    # POST请求参数（表单参数参数）
    print(request.POST)
    return render(request,'art/list.html',context={'name':'hu','age':0})

