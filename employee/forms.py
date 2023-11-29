from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile
from django.forms.widgets import FileInput

input_class = "block border border-grey-light w-full p-3 rounded mb-4"

# Admin details - gauthamsuper:Adminauth1

class NewUserForm(UserCreationForm):
	
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'email@domain.com','class':input_class}))
	
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'Password', 'class':input_class})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm Password', 'class':input_class})
        self.fields['username'].widget.attrs.update({'placeholder':self.fields['username'].help_text, 'class':input_class})


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 8:
            raise ValidationError(
                message="The username field is less than 8 characters.",
                code='length_mismatch'
            )
        return username

login_class = "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'placeholder':'Enter your Password', 'class':login_class})
        self.fields['username'].widget.attrs.update({'placeholder':self.fields['username'].help_text, 'class':login_class})

    class Meta:
        model = User
        fields = ("username", "password")
        


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':input_class})
        self.fields['last_name'].widget.attrs.update({'class':input_class})
        self.fields['phone_number'].widget.attrs.update({'placeholder':'Mobile Number', 'class':input_class})
        self.fields['city'].widget.attrs.update({'placeholder':'Ex: Bengaluru', 'class':input_class})
        self.fields['state'].widget.attrs.update({'class':input_class})
        self.fields['zipcode'].widget.attrs.update({'placeholder':'Ex: 560056', 'class':input_class})
        self.fields['gender'].widget.attrs.update({'class':input_class})
        self.fields['address'].widget.attrs.update({'class':input_class})

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_pic': FileInput(attrs={'class':"block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"})
        }

    