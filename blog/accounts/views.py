from django.shortcuts import render,redirect
from .forms import User_detailForm
from django.contrib.auth import authenticate
from user.models import User_details
from django.contrib import messages
# Create your views here.


def register(request):
    form=User_detailForm()
    if request.method=='POST':
        username=request.POST.get('username')
        user=User_details.objects.filter(username=username).exists()
        if not user:
            form=User_detailForm(request.POST,request.FILES)
            if  form.is_valid():
                form.save()
                return redirect('login_user')
        else:
            messages.error(request,'Username Already Exist')
    return render(request,'accounts/register.html',{'form':form})

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User_details.objects.filter(username=username,password=password)
        user_details=User_details.objects.get(username=username)
        if user:
            if user_details.usertype =='user':
                return redirect('user_post')
            else:
                return redirect('admin_home')    

        else:
            messages.error(request,'invalid credentials')
            return redirect('login_user')

    return render(request,'accounts/login_user.html')

def Forgot_Password(request):
    return render(request,'accounts/Forgot_Password.html')