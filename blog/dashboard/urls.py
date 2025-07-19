from django.urls import path
from . import views
urlpatterns = [

path('',views.users_list,name='users_list'),
path('users_profile/<int:id>',views.users_profile,name='users_profile'),
path('users_activity/<int:id>',views.users_activity,name='users_activity'),
path('delete_user/<int:id>',views.delete_user,name='delete_user'),
path('search_users/',views.search_users,name='search_users'),
path('blocked_user/<int:id>',views.blocked_user,name='blocked_user'),
path('blocked_list/',views.blocked_list,name='blocked_list'),
path('blog_posts/',views.blog_posts,name='blog_posts')
]
