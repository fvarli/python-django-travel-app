from  django.http import HttpResponse
from django.shortcuts import render
from home.models import Settings

# Create your views here.
def index(request):

    settings = Settings.objects.get(pk=1)
    context = {'settings': settings, 'page':'home'}
    return render(request, 'index.html', context)


def hakkimizda(request):

    settings = Settings.objects.get(pk=1)
    context = {'settings': settings, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):

    settings = Settings.objects.get(pk=1)
    context = {'settings': settings, 'page':'referanslar'}
    return render(request, 'referanslar.html', context)

def iletisim(request):

    settings = Settings.objects.get(pk=1)
    context = {'settings': settings, 'page':'iletisim'}
    return render(request, 'iletisim.html', context)
