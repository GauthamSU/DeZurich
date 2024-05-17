from typing import Any, Optional
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from .models import UserProfile, EmployeeLeave
from django.forms.widgets import FileInput, RadioSelect
from django_flatpickr.widgets import DatePickerInput


input_class = "block border border-grey-light w-full p-3 rounded mb-4"

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



class CustomDatePickerInput(DatePickerInput):
    def set_options(self, options):
        super().__init__(options=options)
        

class ApplyLeaveForm(forms.ModelForm):
    

    class Meta:
        model = EmployeeLeave
        fields = ['leave_type', 'leave_details', 'leave_start_date', 'leave_end_date']
        widgets = {
            'leave_start_date': CustomDatePickerInput(),
            'leave_end_date': CustomDatePickerInput(range_from="leave_start_date")
            }

    def __init__(self, *args, **kwargs):
        employee = kwargs.pop('employee', None)
        super(ApplyLeaveForm, self).__init__(*args, **kwargs)
        if employee:
            self.instance.employee = employee




    # def clean(self):
    #     cleaned_data = super().clean()
    #     print(cleaned_data)
    #     leave_dates = cleaned_data.get('leave_start_date', None)
    #     if leave_dates:
    #         leave_end_date = leave_dates.split()[-1]
    #         leave_start_date = leave_dates.split()[0]
    #         cleaned_data['leave_end_date'] = leave_end_date
    #         cleaned_data['leave_start_date'] = leave_start_date
    #     return cleaned_data
    

    # def save(self, commit=True):
    #     leave_data = super(ApplyLeaveForm, self).save(commit=False)
    #     leave_dates = self.cleaned_data.get('leave_start_date', None)
    #     leave_end_date = leave_dates.split()[-1]
    #     leave_data.leave_end_date = leave_end_date
    #     if commit:
    #         leave_data.save()
    #     return leave_data