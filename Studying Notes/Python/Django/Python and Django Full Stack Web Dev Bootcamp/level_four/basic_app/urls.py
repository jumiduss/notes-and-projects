from django.urls import path
from basic_app import views

app_name = 'basic_app' #set global variable to application name

urlpatterns= [ #Says if you go to anything /relative it gives you relative page view.
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]