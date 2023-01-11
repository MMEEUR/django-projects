from django.shortcuts import render
from projects.models import Project

def homeView(request):
    projects = Project.objects.all()[:3]
    
    return render(request, 'home/index.html', {'projects': projects})