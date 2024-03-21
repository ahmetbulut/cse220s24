from django.http import HttpResponse
from django.shortcuts import render
from secondapp.models import Customer

# Create your views here.
def example(request):
    #return HttpResponse("This is a fine day.")
    return render(request, 'example.html',
                  context={'message': 'keep it cool!',
                           'list_x': ['Harry Potter', 'Sicario', 'The Revenant', 'Zootropolis']})

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