from django.urls import path
from . import views

#отслеживание пути пользователя
urlpatterns = [
    path('', views.home, name='home'),
    path('about_company', views.about_company, name='about_company')
]
