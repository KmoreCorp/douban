from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('people/', views.people, name='people'),
    path('login/', views.account_login, name='login'),
    path('logout/', views.account_logout, name='logout'),
    path('register/', views.account_register, name='register'),
]
