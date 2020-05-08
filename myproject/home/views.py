import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Settings, ContactFormMessage, ContactFormu
from content.models import Content, Category, Images, Comment
from home.forms import SearchForm, SignUpForm
from django.views import View


# Create your views here.


def index(request):

    settings = Settings.objects.get(pk=1)
    slider_data = Content.objects.all()[:4]
    random_contents = Content.objects.order_by('?')[:6]
    random_category = Category.objects.order_by('?')[:10]
    category = Category.objects.all()
    context = {'settings': settings,
               'category': category,
               'random_category': random_category,
               'page': 'home',
               'slider_data': slider_data,
               'random_contents': random_contents}
    return render(request, 'index.html', context)


class Hakkimizda(View):
    def get(self, request):
        settings = Settings.objects.get(pk=1)
        category = Category.objects.all()
        context = {'settings': settings, 'category': category}
        return render(request, 'hakkimizda.html', context)


def referanslar(request):

    settings = Settings.objects.get(pk=1)
    category = Category.objects.all()
    context = {'settings': settings, 'category': category}
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


def content_detail_menu(request, id, slug):
    category = Category.objects.all()
    content = Content.objects.filter(categry_id=id)
    link = '/content/' + str(content[0].id) + '/' + content[0].slug
    return HttpResponse(link)
    #return HttpResponseRedirect(link)


def content_search(request):
    if request.method == 'POST':    # check form post
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']  # get form data
            #catid = form.cleaned_data['catid']  # get form data
            contents = Content.objects.filter(title__icontains=query)  # select * from content where title like %query%

            '''
                        if catid == 0:
                contents = Content.objects.filter(title__icontains=query)   # select * from content where title like %query%
            else:
                contents = Content.objects.filter(title__icontains=query, category_id=catid)
                
            '''

            # return HttpResponse(content)
            context = {'contents': contents,
                       'category': category}
            return render(request, 'contents_search.html', context)

        return HttpResponseRedirect('/')


def content_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        contents = Content.objects.filter(title__icontains=q)
        result = []
        for rs in contents:
            content_json = {}
            content_json = rs.title
            result.append(content_json)
        data = json.dumps(result)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

        else:
            messages.warning(request, "Giriş bigileriniz hatalı. Tekrar deneyin.")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'login.html', context)


def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')

    form = SignUpForm()

    category = Category.objects.all()
    context = {'category': category,
               'form': form}
    return render(request, 'sign_up.html', context)

