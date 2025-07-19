from django.shortcuts import render
from user.models import User_details,Post,Comment
# Create your views here.



def users_list(request):
    users=User_details.objects.filter(usertype='user')
    return render(request,'admin/users_list.html',{'users':users})

def users_profile(request,id):
    if User_details.objects.filter(id=id).exists():
        profile=User_details.objects.get(id=id)
    return render(request,'admin/users_profile.html',{'profile':profile})

def users_activity(request,id):
    if User_details.objects.filter(id=id).exists():
        user_post=Post.objects.filter(author_id=id)
        id=id
        user=User_details.objects.get(id=id)
        user_comments=Comment.objects.filter(posted_by=user)
    return render(request,'admin/users_activity.html',{'user_post':user_post,'user':user,'user_comments':user_comments})