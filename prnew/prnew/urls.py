"""
URL configuration for prnew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newapp import views
from django.conf import settings
from django.urls.conf import include
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('login',views.employlogin,name='login'),
    path('register',views.empregister,name='register'),
    path('dashboard',views.empdash,name='dashboard'),
    path('logout',views.emplogout,name='logout'),
    path('proreg',views.productreg,name='proreg'),
    path('proview',views.productview,name='proview'),
    path('proedit/<int:pk>',views.productupdate,name='proedit'),
    path('prodelete/<int:pk>',views.prodelete,name='prodelete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)