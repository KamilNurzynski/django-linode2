from django.urls import path
from . import views


app_name = 'other'
urlpatterns = [
    path('', views.simple_view),
    path('home/', views.HomeView.as_view(), name='home'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'),
    path('contact/', views.ContactFormView.as_view(), name='contact')
]
