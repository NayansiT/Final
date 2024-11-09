from django import forms
from accounts.models import Application 

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'dob',
            'phone',
            'course',
            'city', 
            'category', 
            'marks',
            'scorecard'
        ]

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 10 or not phone.isdigit():
            raise forms.ValidationError("Phone number must be 10 digits.")
        return phone