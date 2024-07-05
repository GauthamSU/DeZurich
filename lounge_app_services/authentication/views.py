from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import NewUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup(request):
    form = NewUserForm()
    if request.user.is_authenticated:
        return redirect('workspace')
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been successfully created.')
            return redirect('login')
        else:
            context = {'form':form}
            response = render(request, 'authentication/partials/htmx_partials.html#form-error-partial', context)
            response['HX-Retarget'] = '#form-error-list'
            return response   

    context = {'form':form}
    return render(request, 'authentication/signup.html', context)


def user_login(request):
    form = LoginForm(request)
    if request.user.is_authenticated:
        return redirect('workspace')
    if request.htmx:
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('workspace')
            else:
                context = {'form':form}
                response = render(request, 'authentication/partials/htmx_partials.html#form-error-partial', context)
                response['HX-Retarget'] = '#form-error-list'
                response['HX-Reselect'] = '.errorlist'
                return response
        else:
            context = {'form':form}
            return render(request, 'authentication/partials/login_element_partial.html#login-form-partial', context)
    
    context = {'form':form}
    return render(request, 'authentication/login.html', context)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')
