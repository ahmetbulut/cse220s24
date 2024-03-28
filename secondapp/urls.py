from django.urls import path
from secondapp.views import create_movie, get_customers, rate_view

urlpatterns = [
    path('create_movie', create_movie),
    path('search', get_customers),
    path('rate', rate_view),
]