from django.http import HttpResponse
from django.shortcuts import render
from secondapp.models import Customer, Movie, Rating
from secondapp.forms import MovieForm, RatingForm


from plotly.offline import plot
from plotly.graph_objs import Scatter, Bar

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
        if 'button' in request.POST:
            if request.POST['button'] == 'cancel':
                return render(request, 'sampleform.html',
                              context={'error': 'Operation Cancelled!'})
            elif request.POST['button'] == 'plotly-demo':
                x_data = [1, 2, 3, 4, 5, 8, 10, 15, 20, 33, 50, 60, 70, 90]
                y_data = [14, 11, 5, 16, 1, 1, 1, 5, 2, 3, 100, 5, 15, 90]

                plot_div = plot([Bar(x=x_data, y=y_data,
                                     name='Our First Graph in Plotly',
                                     opacity=1.0, marker_color='blue')],
                                output_type='div', include_plotlyjs=False)
                return render(request, 'plot.html', context={'plot_div':plot_div})
    return render(request, 'sampleform.html')
