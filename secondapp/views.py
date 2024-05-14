from django.http import HttpResponse
from django.shortcuts import render
from secondapp.models import Customer, Movie, Rating
from secondapp.forms import MovieForm, RatingForm


# Create your views here.
def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = Movie()
            movie.name = form.cleaned_data['name']
            movie.description = form.cleaned_data['description']
            movie.release_date = form.cleaned_data['release_date']
            movie.save()
            return render(request, 'confirmation.html',
                          context = {'descriptive_info': str(movie)})
    else: # request.method is a GET (the first time get)
        form = MovieForm()

    return render(request, 'create_movie.html', context = {'form': form})

def get_customers(request):
    if request.GET:
        customers = Customer.objects.filter(name__contains=request.GET['name_filter'])
        return render(request,"search.html",
                  context={
                      "user": request.META['USER'],
                      "customers": customers}
                  )
    else:
        return render(request,"search.html")


def rate_view(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            movie = form.cleaned_data['movie']
            rating = form.cleaned_data['rating']
            rate = Rating(customer=customer, movie=movie, rating=rating)
            rate.save()
            return render(request, 'confirmation.html',
                          context={'descriptive_info': str(rate)})
    else:
        form = RatingForm()

    return render(request, 'rate.html', context={'form': form})


def display_sampleform(request):
    if request.method == 'POST':
        return HttpResponse("User typed in %s " % request.POST['user_data'])
    return render(request, 'sampleform.html')
