from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import MyRegisterForm
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'successfully created username for {username}')
            return redirect('blogHome')
        else:
            print('some error')
    else:
        form = MyRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    