from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'base/index.html', context)


def about(request):
    context = {}
    return render(request, 'base/about.html', context)


def services(request):
    context = {}
    return render(request, 'base/services.html', context)

def gallery(request):
    context= {}
    return render(request, 'base/gallery.html', context)
