from  django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text = "Django Kurulumu : python -m pip install -e django <br> Proje Oluşturma : django-admin startproject myproject <br> App Ekleme : python manage.py startapp home"
    context = {'text': text}
    return render(request, 'index.html', context)