from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ApplicationForm 
from accounts.models import Application 

@login_required
def apply(request):
    """Allow the user to apply for a hostel if not already applied."""
    # Check if the user has already applied
    if Application.objects.filter(student=request.user).exists():
        messages.warning(request, "You have already applied for a hostel.")
        application = Application.objects.get(student=request.user)  # Get existing application
        return render(request, 'admissions/apply.html', {
            'application_exists': True,
            'application': application,
        })  # Render with application details

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user  # Set the student field to the logged-in user
            application.save()
            messages.success(request, "Application submitted successfully!")
            return redirect('user_home')  # Redirect to the user home after submission
    else:
        form = ApplicationForm()

    return render(request, 'admissions/apply.html', {'form': form, 'application_exists': False})


