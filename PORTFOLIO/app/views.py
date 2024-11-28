# portfolio/views.py
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

def portfolio_view(request):
    # Fetch all projects from the database
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def add_project(request):
    # Handle the form for adding a new project
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new project to the database
            return redirect('portfolio')  # Redirect to the portfolio view
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})


def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")    