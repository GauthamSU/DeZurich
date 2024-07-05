from django.shortcuts import render

# Create your views here.
def workspace_view(request):
    response = render(request, 'workspace/workspace.html')
    response['HX-Refresh'] = 'true'
    return response