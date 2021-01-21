from django.contrib.auth import authenticate,login,forms,models
from django import forms as f

class RegisterForm(forms.UserCreationForm):
    email = f.EmailField()
    
    class Meta:
        model = models.User
        fields = ["username", "email", "password1", "password2"]
