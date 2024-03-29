from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")
def index(request):
    user_list = User.objects.order_by('lname') #order_by is a common SQL command
    user_dict = {'user':user_list}

    return render(request,'first_app/index.html',context=user_dict)
