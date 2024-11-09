from django.urls import path
from .views import apply, application_status  # Import your views

urlpatterns = [
    path('apply/', apply, name='apply'),  # URL for the apply view
    path('status/', application_status, name='application_status'),  # URL for the application status
]