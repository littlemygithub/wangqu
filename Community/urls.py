"""Community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from website import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('index/',views.index),
    path('home_test/',views.home_test),
    path('source/',views.source),
    path('people/',views.people),
    re_path(r'^people-(\d+)/',views.people),
    path('about/',views.about),
    path('art/',views.art),
    path('community/',views.community),
    path('login/',views.login),
    re_path(r'^login_source-(\d+)/',views.login_source),
    # path('login_people/',views.login_people),
    re_path(r'login_people-(\d+)/',views.login_people),

]
