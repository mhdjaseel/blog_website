from django.shortcuts import render,redirect
from .models import User_details,Post,Comment
from accounts.forms import User_detailForm
# Create your views here.

def home(request):
    return render(request,'user/layout.html')

def user_post(request):
    return render(request,'user/user_post.html')

def user_profile(request):
    user_id=request.session.get('user_id')
    user=User_details.objects.get(id=user_id)
    if request.method =='POST':
        form=User_detailForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            updated_user = form.save()
            request.session['username']=updated_user.username
            return redirect('post_view')
    else:
        form=User_detailForm(instance=user)

    return render(request,'user/user_profile.html',{'form':form})

def create_post(request):
    return render(request,'user/create_post.html')

def post_view(request):
    return render(request,'user/post_view.html')