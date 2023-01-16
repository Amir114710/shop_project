from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register' , views.RegisterationView.as_view() , name="register"),
    path('check_otp' , views.CheckOtpCode.as_view() , name="check_otp"),
    path('login' , views.LoginUserView.as_view() , name='login'),
    path('logout' , views.logout_user , name='logout'),
]

