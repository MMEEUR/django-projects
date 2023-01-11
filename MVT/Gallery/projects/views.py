from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
# Create your views here.
'''
@login_required
def projectView(request):
    
    if request.method == 'POST':
        form = ProjectForm(data=request.POST)
        if form.is_valid:
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            
            return redirect(new_item.get_absolute_url())
        
    else:
        form = ProjectForm(data=request.GET)
        
    return render(request, 'projects/create.html', {'section': 'images', 'form': form})
'''

def projectView(request):
    projects = Project.objects.all()
    
    return render(request, 'projects/project_list.html', {'projects': projects})

def projectDetailView(request, year, month, day, slug):
    project = get_object_or_404(Project, slug=slug, created__year=year, created__month=month, created__day=day)
    similar_projects = Project.objects.filter(grouping=project.grouping)[:3]
    
    return render(request, 'projects/project_detail.html', {'project': project, 'similar_projects': similar_projects})
    