from django.urls import path
from recommendation import views

urlpatterns = [
   
    path("",views.home,name='home'),
    path("About/",views.about,name='about'),
    path("service/",views.service,name='service'),
    path("About/service/",views.service,name='service'),
    path("service/About/",views.about,name='about'),
    path("login/",views.login,name='login'),
    path("signup/",views.signup,name='signup'),
    
   
]
