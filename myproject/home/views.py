from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Settings, ContactFormMessage, ContactFormu
from content.models import Content, Category, Images, Comment

# Create your views here.


def index(request):

    settings = Settings.objects.get(pk=1)
    slider_data = Content.objects.all()[:4]
    random_contents = Content.objects.all().order_by('?')[:4]
    random_category = Category.objects.all().order_by('?')[:8]
    category = Category.objects.all()
    context = {'settings': settings,
               'category': category,
               'random_category': random_category,
               'page': 'home',
               'slider_data': slider_data,
               'random_contents': random_contents}
    return render(request, 'index.html', context)


def hakkimizda(request):

    settings = Settings.objects.get(pk=1)
    context = {'settings': settings, 'page': 'hakkimizda'}
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
    context = {'settings': settings,
               'form': form}
    return render(request, 'iletisim.html', context)


def category_contents(request, id, slug):
    category = Category.objects.all()
    category_data = Category.objects.get(pk=id)
    contents = Content.objects.filter(category_id=id)
    context = {'contents': contents,
               'category': category,
               'category_data': category_data}
    return render(request, 'geziler.html', context)


def content_detail(request, id, slug):
    category = Category.objects.all()
    content = Content.objects.get(pk=id)
    images = Images.objects.filter(content_id=id)
    comments = Comment.objects.filter(content_id=id, status='True')
    context = {'category': category,
               'images': images,
               'comments': comments,
               'content': content}
    return render(request, 'content_detail.html', context)
