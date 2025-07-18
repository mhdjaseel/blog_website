from django.shortcuts import render,redirect,get_object_or_404
from .models import User_details,Post,Comment
from accounts.forms import User_detailForm
from.forms import PostForm
from django.db.models import Q
# Create your views here.



def user_post(request):
    user_id=request.session.get('user_id')
    if user_id:
        user_posts=Post.objects.filter(author_id=user_id).order_by('-created_at')
    return render(request,'user/user_post.html',{'user_posts':user_posts})

def user_profile(request):
    user_id=request.session.get('user_id')
    user=User_details.objects.get(id=user_id)
    if request.method =='POST':
        form=User_detailForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            updated_user = form.save()
            request.session['username']=updated_user.username
            request.session['profile_img']=updated_user.profile_img.url
            return redirect('post_view')
    else:
        form=User_detailForm(instance=user)

    return render(request,'user/user_profile.html',{'form':form})

def create_post(request):
    if request.method=='POST':
        username=request.session.get('username')
        user=get_object_or_404(User_details,username=username)
        image=request.FILES.get('image')
        description=request.POST.get('description')
        if description and image: 
            Post.objects.create(author=user,image=image,description=description)
            return redirect('user_post')
    return render(request,'user/create_post.html')

def post_view(request):
    user_posts=Post.objects.all().order_by('-created_at')
    return render(request,'user/post_view.html',{'user_posts':user_posts})

def edit_post(request,id):
    if Post.objects.filter(id=id).exists():
        post=Post.objects.get(id=id)
        if request.method=='POST':
            user_posts=PostForm(request.POST,request.FILES,instance=post)
            if user_posts.is_valid():
                user_posts.save()
                return redirect('user_post')
        else:
            user_posts=PostForm(instance=post)
    return render(request,'user/edit_post.html',{'user_posts':user_posts})

def search(request):
    query=''
    post=[]
    if 'q' in request.GET:
        query=request.GET.get('q')
        post=Post.objects.filter(author__username__icontains=query)
    context={
        'query':query,
        'post':post
    }
    return render(request,'user/search.html',context)