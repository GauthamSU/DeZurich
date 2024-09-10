from django.shortcuts import render
from lounge_app_services.workspace.plotly_charts import leave_type_chart

def workspace_view(request):
    leave_plot = leave_type_chart(request)
    response = render(request, 'workspace/workspace.html', context={'leave_plot':leave_plot})
    response['HX-Refresh'] = 'true'
    return response