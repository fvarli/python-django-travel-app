from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Settings, ContactFormMessage, ContactFormu

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

    if request.method == 'POST':    # if form is posted
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()   # connect with model
            data.name = form.cleaned_data['name']   #get data form the form
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()     # save to database
            messages.success(request, "Mesajınız başarıyla gönderişmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')



    settings = Settings.objects.get(pk=1)
    form = ContactFormu()
    context = {'settings': settings, 'form':form}
    return render(request, 'iletisim.html', context)
