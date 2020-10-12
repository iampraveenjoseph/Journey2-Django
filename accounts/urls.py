from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    #path('activate',VerificationView.as_view(),name="activate")
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('complete',views.home,name='complete'),
   # path('activate/<uidb64>/<token>/returnHome',views.home, name='returnHome')
  #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        #views.activate, name='activate')
    ]