from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name="user_update"),
    path('password/', views.change_password, name="change_password")

    #path('add_comment/<int:id>', views.add_comment, name="add_comment")
]