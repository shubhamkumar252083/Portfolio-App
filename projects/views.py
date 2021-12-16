from django.shortcuts import render
import os
from .models import Project

absolute_path = os.path.abspath(__file__)
dir_path = os.path.dirname(absolute_path)


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        "dir_path": dir_path,
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        "dir_path": dir_path,
    }
    return render(request, 'project_detail.html', context)
