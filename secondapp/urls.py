from django.urls import path
from secondapp.views import create_movie, get_customers, rate_view, display_sampleform

urlpatterns = [
    path('create_movie', create_movie),
    path('search', get_customers),
    path('rate', rate_view),
    path('register', display_sampleform),
    path('dosomething', display_sampleform)
]