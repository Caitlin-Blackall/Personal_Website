from django.shortcuts import render
from projects.models import Project

# Create your views here.
# create a query to retrieve all objects in the projects table
# define context dictionary
# render the template with context as an argument
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)