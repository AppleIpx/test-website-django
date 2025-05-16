from django.urls import path

from . import views

# отслеживание пути пользователя
urlpatterns = [
    path("", views.home, name="home"),
    path("about_company", views.about_company, name="about_company"),
    path("iphone", views.iphone_view, name="iphone"),
    path("macbook", views.macbook_view, name="macbook"),
    path("airpods", views.airpods_view, name="airpods"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
]
