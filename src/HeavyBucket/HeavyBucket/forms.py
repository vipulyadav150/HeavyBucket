from django import forms
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model





User = get_user_model()
class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100,widget=forms.TextInput(
                                            attrs={'class':'form-control','placeholder':'Your name here',
                                                   'id':'fullname'}
                                                    ),help_text="Max 100 characters")
    email = forms.EmailField(widget=forms.TextInput(
                                            attrs={'class':'form-control','placeholder':'Your email here',
                                                   'id':'email'}
                                                    ))
    content = forms.CharField(max_length=300,widget=forms.Textarea(attrs={'class':'form-control',
                                                           'placeholder':'Leave your message here',
                                                           'id':'content'}),
                              help_text='300 characters max')


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not 'gmail.com' in email:
            raise forms.ValidationError("Email must be Gmail id!")
        return email



