from django.shortcuts import render


# ответ сервера, что именно показывать, когда пользователь нажимает на какие либо кнопки
# в зависимости от url, что показывать пользователю


def home(request):
    return render(request, "main/home.html")


def about_company(request):
    return render(request, "main/about_company.html")


def iphone_view(request):
    return render(request, "main/iphone.html")


def macbook_view(request):
    return render(request, "main/macbook.html")


def airpods_view(request):
    return (render(request, "main/airpods.html"),)


def login_view(request):
    return render(request, "main/login.html")


def register_view(request):
    return render(request, "main/register.html")
