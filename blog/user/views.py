from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'user/layout.html')

def user_post(request):
    return render(request,'user/user_post.html')

def user_profile(request):
    return render(request,'user/user_profile.html')

def create_post(request):
    return render(request,'user/create_post.html')

def post_view(request):
    return render(request,'user/post_view.html')