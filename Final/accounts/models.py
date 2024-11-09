from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')    
    def __str__(self):
        return self.user.username


class Application(models.Model):
    
    CATEGORY_CHOICES = [
        ('SC', 'Scheduled Castes (SC)'),
        ('ST', 'Scheduled Tribes (ST)'),
        ('OBC', 'Other Backward Classes'),
        ('OG', 'Open/General'),  
    ]  
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    first_name = models.CharField(max_length=30, default='')  
    middle_name = models.CharField(max_length=30, blank=True, default='')  
    last_name = models.CharField(max_length=30, default='') 
    dob = models.DateField(auto_now_add=False, default='')  
    phone = models.CharField(max_length=10, default='0000000000')  
    course = models.CharField(max_length=50, default='General Course') 
    city = models.CharField(max_length=100, default='City Name')  
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='OG')  
    marks = models.FloatField(default=0.0)  
    scorecard = models.FileField(upload_to='scorecards/', default='default_scorecard.pdf')  
    
    application_date = models.DateTimeField(auto_now_add=True)  # Automatically set when the application is created
    submission_date = models.DateTimeField(null=True)  # When the application was submitted
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending') 

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.category}"