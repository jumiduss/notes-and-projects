from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from appTwo.forms import UserSignup

# Create your views here.
# def index(request):
#     return HttpResponse("<em>My Second Project</em>")

def home_page(request):
    return render(request,'appTwo/home_page.html')

def signup_page(request):
    form = UserSignup()
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'appTwo/home_page.html')
    return render(request,'appTwo/signup_page.html',{'form':form})