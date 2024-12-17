from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    path('', views.AboutUs.as_view(), name='about'),
]