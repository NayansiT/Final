from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User 
from .models import Application
from .forms import UserRegistrationForm 

def home_view(request):
    """
    Render the home page with login and registration options.
    """

    return render(request, 'home/home.html') 


def register(request):
    """
    User registration view to handle new user sign-ups.
    If registration is successful, redirect to the home page.
    """
    if request.method == 'POST':
        # Create form instance with POST data
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            form.save()
            messages.success(request, "Registered successfully! You can now log in.")
            return redirect('home')
    else:
        form = UserRegistrationForm()  # Create an instance of the form for GET requests
    
    return render(request, 'accounts/register.html', {'form': form})  # Pass the form to the template




def login_view(request):
    """
    Custom login view to authenticate and log in users.
    If login is successful, redirect to the user dashboard.
    """
    if request.method == 'POST':
        
        # Get username and password from POST request
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_home')  # Redirect to user dashboard after login
        else:
            # Display error message if login fails
            messages.error(request, 'Invalid username or password')
    # Render login template if GET request or login fails
    return render(request, 'accounts/login.html')  

@login_required
def user_home(request):
    """
    Render the user dashboard.
    """
    try:
        application = Application.objects.get(student=request.user)
    except Application.DoesNotExist:
        application = None  # No application found

    return render(request, 'accounts/user_home.html', {'application': application})