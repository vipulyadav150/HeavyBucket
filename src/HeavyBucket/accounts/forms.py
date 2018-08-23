from django import forms
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    #Unique username constraint setup
    def clean_username(self):
        username = self.cleaned_data.get('username')
        #Queryset to get all logged in or registered user objects from User model
        user_queries = User.objects.filter(username=username)#Got all usernames that are already registered
        #Checking if current username matches any other username from the results
        if user_queries.exists():
            raise forms.ValidationError('Username Exists!')
        return username

    # Unique email id constraint setup
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_queries = User.objects.filter(email=email)
        if email_queries.exists():
            raise forms.ValidationError('This Email Id is taken!')
        return email


    #Password confirmation during registration
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirmation_password = self.cleaned_data.get('confirm_password')

        if password!=confirmation_password:
            raise forms.ValidationError("Passwords must match!")
        return data





class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

