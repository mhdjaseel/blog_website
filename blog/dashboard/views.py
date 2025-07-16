from django.shortcuts import render

# Create your views here.

def admin_home(request):
    return render(request,'admin/admin_home.html')