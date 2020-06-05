from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name="user_update"),
    path('password/', views.change_password, name="change_password"),
    path('add_new_trip/', views.add_new_trip, name="add_new_trip"),
    path('add_new_category/', views.add_new_category, name="add_new_category"),
    path('categories/', views.categories, name="categories"),
    path('edit_category/<int:id>', views.edit_category, name="edit_category"),
    path('delete_category/<int:id>', views.delete_category, name="delete_category"),
    path('comments/', views.comments, name="comments"),
    path('delete_comment/<int:id>', views.delete_comment, name="delete_comment"),

    path('add_content/', views.add_content, name="add_content"),
    path('contents/', views.contents, name="contents"),
    path('edit_content/<int:id>', views.edit_content, name="edit_content"),
    path('delete_content/<int:id>', views.delete_content, name="delete_content"),
    path('content_add_image/<int:id>', views.content_add_image, name="content_add_image"),
]
