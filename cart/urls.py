from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.get_cart, name='cart'),
    path('add/<int:product_id>', views.add_to_cart, name='add_cart'),
    path('remove/<int:product_id>', views.remove_from_cart, name='remove_cart'),
    ]
