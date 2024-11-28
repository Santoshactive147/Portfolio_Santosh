# portfolio/views.py
from django.shortcuts import render, redirect
from .models import Project,QueryMessages
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


from django.shortcuts import render, redirect
from .models import QueryMessages

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         print(name)
#         email = request.POST.get('email')
#         message = request.POST.get('message')
        
#         # Save the data to QueryMessages model
#         QueryMessages.objects.create(name=name, email=email, message=message)
        
#         # Redirect to thank you page
#         return redirect('thankyou')
    
#     return render(request, 'contact.html')
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            print(name)
            email = request.POST.get('email')
            message = request.POST.get('message')

            print(f"Name: {name}, Email: {email}, Message: {message}")  # Debugging print

            # Save the data to QueryMessages model
            QueryMessages.objects.create(name=name, email=email, message=message)
            
            # Redirect to thank you page
            return redirect('thankyou')
        except Exception as e:
            print(f"Error: {e}")  # Log the error
            return HttpResponse("An error occurred while saving the data.")

    return render(request, 'contact.html')

def about(request):
    return render(request,"about.html")    


def thankyou(request):
    return render(request, 'thankyou.html')
    


def query_messages(request):
    messages = QueryMessages.objects.all()
    return render(request, 'querymessages.html', {'messages': messages})
