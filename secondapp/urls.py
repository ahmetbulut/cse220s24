from django.urls import path
from secondapp.views import example, get_customers

urlpatterns = [
    path('example', example),
    path('search', get_customers)
]