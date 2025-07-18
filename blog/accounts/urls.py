from django.urls import path
from . import views
urlpatterns = [
path('',views.register,name='register'),
path('login_user/',views.login_user,name='login_user'),
path('Forgot_Password/',views.Forgot_Password ,name='Forgot_Password'),
path('reset_password/<int:user_id>/',views.reset_password,name='reset_password'),
path('user_logout',views.user_logout,name='user_logout')
]
