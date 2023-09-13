from django.contrib import admin
from django.urls import path, include

# переход между страницами
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
    # path('about_company', include('main.urls'))
]
