from django.urls import path
from .views import *

urlpatterns = [
    path('' , home , name='home'),
    path('your_clubs' , your_clubs , name='your_clubs'),
    path('all_clubs' , all_clubs , name='all_clubs' ),
    path('sign-up' , signup_page , name='sign_up' ),
    path('login' , login_page , name='login')
]