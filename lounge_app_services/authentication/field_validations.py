from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from .forms import NewUserForm

template_html = "authentication/partials/htmx_partials.html"
user = get_user_model()
            
def check_username(request):
    
    partial_template = f'{template_html}#username-notifier-partial'
    user_exists = 'This username already exists. Create an unique username.'
    valid_username = 'This username is available.'

    if request.htmx:
        if request.method == 'POST':
            
            username = request.POST.get('username')
            username_validators = user._meta.get_field('username').validators
            
            try:
                for validator in username_validators:
                    validator(username)
                if user.objects.filter(username=username).exists():
                    raise ValidationError(user_exists)               
                return render(request, partial_template, {'template_message':valid_username, 'colour': 'green'})
            
            except ValidationError as val_error:
                return render(request, partial_template, {'template_message':val_error.messages[0], 'colour': 'red'})
            

def check_email(request):
    
    partial_template = f'{template_html}#email-notifier-partial'
    valid_email_message = "This email is valid."
    email_exists = "This email is already registered, kindly use a different email."
    
    if request.htmx:
        if request.method == 'POST':
            email = request.POST.get('email')
            try:
                validate_email(email)
                if user.objects.filter(email=email).exists():
                    print(user.objects.filter(email=email).values_list())
                    raise ValidationError(email_exists)
                return render(request, partial_template, {'template_message':valid_email_message, 'colour': 'green'})
            except ValidationError as val_error:
                return render(request, partial_template, {'template_message':val_error.messages[0], 'colour': 'red'})
    

def check_password1(request):
    
    partial_template = f'{template_html}#password1-notifier-partial'
    
    if request.htmx:
        if request.method == 'POST':
            password = request.POST['password1']
            
            try:
                password_validation.validate_password(password)
                return render(request, partial_template, {'template_message':'', 'colour': 'red'})
            except ValidationError as val_error:
                return render(request, partial_template, {'template_message':val_error.messages[0], 'colour': 'red'})

    

def check_password2(request):
    
    partial_template = f'{template_html}#password2-notifier-partial'
    password_match_error = 'Both passwords does not match with each other'

    if request.htmx:
        if request.method == 'POST':
            password2 = request.POST.get('password2')
            password1 = request.POST.get('password1')
            try:
                if password2 != password1:
                    raise ValidationError(password_match_error)
                return render(request, partial_template, {'template_message':'', 'colour': 'red'})
            except ValidationError as val_error:
                return render(request, partial_template, {'template_message':val_error.messages[0], 'colour': 'red'})