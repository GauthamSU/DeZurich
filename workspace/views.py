from django.shortcuts import render

# Create your views here.
def workspace_view(request):
    return render(request, 'workspace/workspace.html')