from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm      
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #saves the password with the hash
            user.save() #saves the hashed password to the database

            profile = profile_form.save(commit=False)
            profile.user = user #This sets up the OneToOne relationship in the UserProfileInfo model
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True

            else:#One of the forms were invalid
                print(user_form.errors,profile_form.errors)    

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'basic_app/registration.html',
                            {'user_form':user_form,'profile_form':profile_form,'registered':registered})

#Create a new view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username') #username defined in the html
        password = request.POST.get('password')

        user = authenticate(username=username,password=password) #define them inside function call to avoid errors

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(usernmae,password))
            return HttpResponse("Invalid login details suppplied!")

    else:
        return render(request, "basic_app/login.html",{})

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required #This HAS to be on the line directly above the function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))