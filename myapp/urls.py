from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('sentmessage/', views.sentmessage, name='sentmessage'),
    path('request/', views.request_view, name='request'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    
]