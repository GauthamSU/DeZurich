from datetime import timedelta
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ProfileForm, ApplyLeaveForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EmployeeLeave
from django_flatpickr.schemas import FlatpickrOptions


# To get a list of dates in string format between a date range.
def get_dates_between(start_date, end_date):
    delta = end_date - start_date
    date_list = [str(start_date + timedelta(days=i)) for i in range(delta.days + 1)]
    return date_list




@login_required(login_url='login')
def user_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_card')
        else:
            print(profile_form.errors)
    else:
        profile_form = ProfileForm(instance=profile)
    context = {'profile_form':profile_form}
    return render(request, 'employee/profile.html', context)


@login_required(login_url='login')
def profile_card(request):
    profile = request.user.userprofile
    context = {'profile':profile}
    return render(request, 'employee/profile_card.html', context)


@login_required(login_url='login')
def apply_leave(request, pk=None):
    employee = request.user.userprofile
    employee_leaves = EmployeeLeave.objects.filter(employee=employee)
    return_template = "employee/apply_leave.html"
    disable_dates = []

    if request.method == 'POST':

        # Updating the database for pre-existing leaves
        pk_url = request.path_info.split('/')[-2]
        if pk_url != 'employee_leave':
            instance = employee_leaves.get(id=int(pk_url))
            form = ApplyLeaveForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('apply_leave')
        
        # Creaing a new leave request and updating it to the database
        form = ApplyLeaveForm(request.POST, employee=employee)
        if form.is_valid():
            form.save()
            return redirect('apply_leave')
    else:

        # Re-rendering the view for htmx request of a previous submitted leave application
        if pk:
            instance = employee_leaves.get(id=int(pk))
            form = ApplyLeaveForm(instance=instance)
            for leave in employee_leaves:
                if leave != instance:
                    disable_dates += get_dates_between(leave.leave_start_date, leave.leave_end_date)
            return_template = "employee\leave_partials\leave_application_form.html"
        
        # Rendering raw leave application form with dates of previous submissions disabled
        else:
            form = ApplyLeaveForm()
            for leave in employee_leaves:
                disable_dates += get_dates_between(leave.leave_start_date, leave.leave_end_date)
            
        # Updating the flatpickr widget options to make specific dates disabled.
        form.fields['leave_start_date'].widget.set_options(FlatpickrOptions(disable=disable_dates))
        form.fields['leave_end_date'].widget.set_options(FlatpickrOptions(disable=disable_dates))
        
    context = {'form':form, 'employee_leaves':employee_leaves}
    return render(request, return_template, context)


def remove_leave_request(request, pk):
    leave_instance = EmployeeLeave.objects.get(id=int(pk))
    leave_instance.delete()
    return redirect('apply_leave')