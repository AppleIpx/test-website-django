from django.shortcuts import render
from django.http import HttpResponse


# ответ сервера, что именно показывать, когда пользователь нажимает на какие либо кнопки
#в зависимости от url, что показывать пользователю

def home(request):
    return render(request, "main/home.html")

def about_company(request):
    return render(request, "main/about_company.html")


#<em>Hello</em>