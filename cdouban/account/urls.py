from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('people/', views.people, name='people'),
]
