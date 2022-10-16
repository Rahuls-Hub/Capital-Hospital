from django.urls import path, include
from user import views
from user.views import Add_Appointment1, View_Appointment1
from user.views import User_Login

urlpatterns = [
    path('',views.index,name="index"),
    path('',include('user.urls')),
    path('user_login/', User_Login,name='user_login'),
    path('register/',views.register,name="register"),
    path('login/',views.User_Login,name="login1"),
    path('add_appointment1/', Add_Appointment1, name='add_appointment1'),
    path('view_appointment1/', View_Appointment1, name='view_appointment1'),
]