from typing import Any, Optional
from django import forms
from .models import UserProfile, EmployeeLeave
from django.forms.widgets import FileInput, RadioSelect
from django_flatpickr.widgets import DatePickerInput


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({'placeholder':'Mobile Number'})
        self.fields['city'].widget.attrs.update({'placeholder':'Ex: Bengaluru'})
        self.fields['zipcode'].widget.attrs.update({'placeholder':'Ex: 560056'})
        

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_pic': FileInput()
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