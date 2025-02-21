from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginUserForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    error = ''
    success = 'Successfully authenticated'
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'mainapp\index.html', {'success': success, 'user': user})
        else:
            error = 'Invalid login'
    else:
        form = LoginUserForm()
    return render(request, 'mainapp\index.html', {'form': form,
                                                  'error': error})