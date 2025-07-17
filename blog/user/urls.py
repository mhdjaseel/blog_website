from django.urls import path
from . import views
urlpatterns = [
path('',views.home,name='home'),
path('user_post/',views.user_post,name='user_post'),
path('user_profile/',views.user_profile,name='user_profile'),
path('create_post',views.create_post,name='create_post'),
path('post_view/',views.post_view,name='post_view'),

    
]
