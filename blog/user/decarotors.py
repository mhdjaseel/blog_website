
from django.shortcuts import redirect

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login_user')  # or your login URL name
        return view_func(request, *args, **kwargs)
    return wrapper