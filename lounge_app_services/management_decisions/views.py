from django.shortcuts import render
from django.db.models import Q
from lounge_app_services.employee.models import UserProfile, EmployeeLeave
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, permission_required



@login_required(login_url='login')
def leave_approval(request, pk=None, action=None):
    employee = request.user.userprofile
    if employee.group.name == 'Management Staff':
        leaves = EmployeeLeave.objects.all()
        # leaves = EmployeeLeave.objects.filter(is_approved=False)
        if request.htmx and action == 'change':
            leave = EmployeeLeave.objects.get(pk=pk)
            leave.is_approved = not leave.is_approved
            leave.save()
            context = {'approved': leave.is_approved}
            return render(request, 'management_decisions/partials/leave_list_table.html#is-approved-td', context)
        elif request.htmx and action == 'revision':
            leave = EmployeeLeave.objects.get(pk=pk)
            if request.method == 'GET':
                return render(request, 'management_decisions/partials/leave_list_table.html#revision-input', {'leave':leave})
            elif request.method == 'POST':
                revision = dict(request.POST)['revision'][0]
                leave = EmployeeLeave.objects.get(pk=pk)
                leave.revision = revision
                leave.save()
                return render(request, 'management_decisions/partials/leave_list_table.html#change-revision-status', {'leave':leave})
        
        leaves = EmployeeLeave.objects.filter(is_approved=False)
        context = {'leaves': leaves}
        return render(request, 'management_decisions/leave_approval.html', context)
    else:
        return HttpResponseForbidden('<h3>You do not have the permissions to access the page</h3>')
    

@login_required(login_url='login')
def search_users(request):
    if request.htmx and request.method == 'GET':
        filter_condition = dict(request.GET)['table-search-users'][0]
        leaves = EmployeeLeave.objects.filter(Q(employee__first_name__icontains=filter_condition) | Q(employee__last_name__icontains=filter_condition))
        return render(request, 'management_decisions/partials/leave_list_table.html#employees-leave-tbody', {'leaves':leaves})