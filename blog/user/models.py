from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class User_details(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img=models.ImageField( upload_to='images/')
    phone_no=models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    author=models.ForeignKey(User_details,on_delete=models.CASCADE)
    image=models.ImageField( upload_to='pictures/')
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    text=models.TextField()
    