from django.urls import path
from . import views

urlpatterns = [
    path('', views.court_home, name='court_home'),
]