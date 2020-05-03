from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('add_comment/<int:id>', views.add_comment, name="add_comment")
]