from django import forms
from secondapp.models import Customer, Movie

# Create a form class.

class MovieForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    release_date = forms.DateField()

class RatingForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    rating = forms.IntegerField()



