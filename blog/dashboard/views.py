from django.shortcuts import render,redirect
from user.models import User_details,Post,Comment
from django.core.paginator import Paginator
# Create your views here.



def users_list(request):
    users=User_details.objects.filter(usertype='user')
    return render(request,'admin/users_list.html',{'users':users})

def users_profile(request,id):
    if User_details.objects.filter(id=id).exists():
        profile=User_details.objects.get(id=id)
    return render(request,'admin/user_profile.html',{'profile':profile})

def users_activity(request,id):
    if User_details.objects.filter(id=id).exists():
        user_post=Post.objects.filter(author_id=id)
        id=id
        user=User_details.objects.get(id=id)
        user_comments=Comment.objects.filter(posted_by=user)
    return render(request,'admin/users_activity.html',{'user_post':user_post,'user':user,'user_comments':user_comments})

def delete_user(request,id):
    user=User_details.objects.get(id=id)
    if request.method=='POST':
        user.delete()
        return redirect('users_list')
    return render(request,'admin/delete_user.html',{'user':user})

def search_users(request):
    if request.method=='GET':
        if 'q' in request.GET:
            query=''
            search_user=[]
            query= request.GET.get('q')
            search_user=User_details.objects.filter(username__icontains=query)      
    return render(request,'admin/search_user.html',{'search_user':search_user})

def blocked_user(request,id):
    user=User_details.objects.get(id=id)
    state=''
    if user.is_active == True:
        state='Block'
    else:
        state='Unblock'
    if user:
            if request.method=='POST':
                if user.is_active == True:
                    user.is_active=False
                    user.save()
                    return redirect('users_list')
                else:
                    user.is_active=True
                    user.save()      
                    return redirect('users_list')
    return render(request,'admin/block_user.html',{'state':state,'user':user})

def blocked_list(request):
    users=User_details.objects.filter(is_active=False)
    return render(request,'admin/blocked_list.html',{'users':users})

def blog_posts(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,2)
    page_no=request.GET.get('page')
    page_obj=paginator.get_page(page_no)
    return render(request,'admin/blog_posts.html',{'page_obj':page_obj})