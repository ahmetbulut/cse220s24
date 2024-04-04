from django.shortcuts import render

def home(request):
    return render(request, 'base.html', context={})

def show_pics(request):
    return render(request, 'pics.html', context={})