from django.shortcuts import render,redirect
from .forms import User_detailForm
from user.models import User_details
from django.contrib import messages
from django.contrib.auth import logout
from user.decarotors import custom_login_required

# Create your views here.


def register(request):
    form=User_detailForm()
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')

        if User_details.objects.filter(username=username).exists():
            messages.error(request,'Username Already Exist')
        elif User_details.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exist')
        else:
            form=User_detailForm(request.POST,request.FILES)
            if  form.is_valid():
                form.save()
                return redirect('login_user')
       
    return render(request,'accounts/register.html',{'form':form})

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User_details.objects.filter(username=username,password=password).exists():
            user_details=User_details.objects.get(username=username)
            if user_details.is_active == False:
                return redirect('user_is_blocked')
            else:
                request.session['user_id'] = user_details.id
                request.session['username'] = user_details.username 
                request.session['profile_img']=user_details.profile_img.url
                if user_details.usertype =='user':
                    return redirect('post_view')
                else:
                    return redirect('users_list')    

        else:
            messages.error(request,'invalid credentials')
            return redirect('login_user')

    return render(request,'accounts/login_user.html')

def Forgot_Password(request):
    if request.method=='POST':
        email=request.POST.get('email')
        if User_details.objects.filter(email=email).exists():
            user=User_details.objects.get(email=email)
            return redirect('reset_password',user_id=user.id)
        else:
            messages.error(request,'Invalid Email')
            return redirect('Forgot_Password')
    return render(request,'accounts/Forgot_Password.html')

def reset_password(request,user_id):  
    user=User_details.objects.get(id=user_id)     
    if request.method=='POST':
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password == cpassword:
            user.password=password 
            user.save()
            return redirect('login_user')
    return render(request,'accounts/reset_password.html')



@custom_login_required
def user_logout(request):
    logout(request)
    return redirect('login_user')

