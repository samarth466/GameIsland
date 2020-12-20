from django.urls import path
from tournaments.views import home

urlpatterns = [
    path('home/{str:code}', home)
]
