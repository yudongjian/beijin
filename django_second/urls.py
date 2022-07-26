
from django.views.static import serve

from app01 import views
from django.urls import path, re_path

from django.contrib import admin
from django.urls import path



handler404 = views.page_not_found
handler500 = views.page_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu),
    path('yewu/', views.yewu),
    path('base', views.base),
    path('2', views.menu2),
    path('menu/', views.menu),

]
