from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import MyRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'successfully created account for {username}')
            return redirect('login')
        else:
            print('some error')
    else:
        form = MyRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
   
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'userForm' : u_form,
        'profileForm': p_form
    }
    profiles = Profile.objects.all()
    return render(request, 'users/profile.html', context)
    