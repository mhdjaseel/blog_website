from django.db import models
from django.utils import timezone
# Create your models here.

USER_TYPE=[
    ('user','user'),
    ('admin','admin')
]

class User_details(models.Model):
    username=models.CharField( max_length=50,unique=True)
    f_name=models.CharField( max_length=50)
    l_name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
    profile_img=models.ImageField( upload_to='images/')
    phone_no=models.BigIntegerField()
    usertype=models.CharField( max_length=50,choices=USER_TYPE,default='user')
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    author=models.ForeignKey(User_details,on_delete=models.CASCADE)
    image=models.ImageField( upload_to='pictures/')
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    text=models.TextField()
    