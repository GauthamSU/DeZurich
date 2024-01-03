from django.shortcuts import redirect, render
from .forms import NewUserForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been successfully created.')
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'employee/signup.html', context)


def user_login(request): 
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('workspace')
    else:
        form = LoginForm(request)
    context = {'form':form}
    return render(request, 'employee/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def user_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_card')
    else:
        profile_form = ProfileForm(instance=profile)
    context = {'profile_form':profile_form}
    return render(request, 'employee/profile.html', context)


@login_required(login_url='login')
def profile_card(request):
    profile = request.user.userprofile
    context = {'profile':profile}
    return render(request, 'employee/profile_card.html', context)

