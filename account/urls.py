from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.phone_number_view, name='phone_number_view'),
    path('enter_otp/<str:phone>/', views.enter_otp_view, name='enter_otp'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('complete_registration/<str:phone>/', views.complete_registration, name='complete_registration'),
]