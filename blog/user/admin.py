from django.contrib import admin

# Register your models here.
from .models import Post,User_details,Comment
admin.site.register(Post)
admin.site.register(User_details)
admin.site.register(Comment)
