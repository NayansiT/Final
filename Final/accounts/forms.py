from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re  #regex module, used for checking patterns like username validity and password complexity

class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label="Name")
    username = forms.CharField(max_length=30, required=True, label="Username")
    email = forms.EmailField(required=True, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken.")
        if not re.match(r'^[\w-]+$', username):  # Allow only alphanumeric and underscores/hyphens
            raise ValidationError("Username can only contain letters, numbers, underscores, and hyphens.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', password):  # Check for uppercase letter
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):  # Check for lowercase letter
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', password):  # Check for digit
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r'[!@#$%^&*()-_=+]', password):  # Check for special character
            raise ValidationError("Password must contain at least one special character.")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['name']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user