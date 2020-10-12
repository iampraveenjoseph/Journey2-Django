from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('find_destination',views.find_destination,name='find_destination'),
    path('feedback',views.feedback,name='feedback')
    
]