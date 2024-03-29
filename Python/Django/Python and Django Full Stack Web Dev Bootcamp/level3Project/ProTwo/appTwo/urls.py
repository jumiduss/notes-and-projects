from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_page, name="signup_page"),
    path('home_page/', views.home_page, name="home_page"),
]
