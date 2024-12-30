# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
]
