from django.urls import path
from . import views
urlpatterns = [

path('',views.users_list,name='users_list'),
path('users_profile/<int:id>',views.users_profile,name='users_profile'),
path('users_activity/<int:id>',views.users_activity,name='users_activity')
    
]
