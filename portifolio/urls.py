from django.urls import path
from . import views

# App's urls go here
app_name = 'portifolio'
urlpatterns = [
    path('', views.index, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('services/', views.services, name= 'services'),
    path('portfolio/', views.portfolio, name= 'portfolio'),
    path('contacts/', views.contacts, name= 'contacts'),
]