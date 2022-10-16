"""HospitalMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path, include
from hospital.views import *
from django.urls import path, include
from user import views
from user.views import Add_Appointment1, View_Appointment1
from user.views import User_Login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    path('about_us/', About_Us,name='about_us'),
    path('', Index, name='home'),
    path('admin_login/', Login,name='login'),
    path('logout/', Logout_admin,name='logout'),
    path('view_doctor/', View_Doctor,name='view_doctor'),
    path('add_doctor/', Add_Doctor,name='add_doctor'),
    path('delete_doctor/<pid>/', Delete_Doctor,name='delete_doctor'),
    path('view_patient/', View_Patient,name='view_patient'),
    path('add_patient/', Add_Patient,name='add_patient'),
    path('delete_patient/<pid>/', Delete_Patient,name='delete_patient'),
    path('add_appointment/', Add_Appointment,name='add_appointment'),
    path('view_appointment/', View_Appointment,name='view_appointment'),
    path('delete_appointment/<pid>/', Delete_Appointment,name='delete_appointment'),
    path('', views.index1, name="index"),
    path('user_login/', User_Login, name='user_login'),
    path('register/', views.register, name="register"),
    path('login1/', views.User_Login, name="login1"),
    path('add_appointment1/', Add_Appointment1, name='add_appointment1'),
    path('view_appointment1/', View_Appointment1, name='view_appointment1'),

]