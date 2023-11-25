from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.base_user import BaseUserManager

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    p = BaseUserManager().make_random_password()
    return render(request, 'generator/password.html', {'password':p})

def about(request):
    return render(request, 'generator/about.html')