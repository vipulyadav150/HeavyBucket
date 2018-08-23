from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model





def home_page(r):
    # print(r.session.get('first_name','Unknown'))  #getter
    #Print session value first name ...if not present then default is Unknown i.e after session ends or log out

    context = {
        'title':'Hello World!',
        'content':'Welcome to the Home Page!'
    }
    if r.user.is_authenticated:
        context['premium_content']='Yeahhhh!'
    return render(r,'home_page.html',context)

def about_page(r):
    context = {
        'title': 'ABOUT PAGE',
        'content': 'Welcome to the About Page!'
    }
    return render(r,'home_page.html',context)

def contact_page(r):
    contact_form = ContactForm(r.POST or None)
    context = {
        'title': 'CONTACT PAGE',
        'content': 'Welcome to the Contact Page!',
        'form':contact_form,
        'brand':'new brand',
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if r.method == 'POST':
    #     print(r.POST)
    #     print(r.POST.get('fullname'))
    #     print(r.POST.get('email'))
    #     print(r.POST.get('content'))
    return render(r,'contacts/view.html',context)

