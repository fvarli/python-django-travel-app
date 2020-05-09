from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


class Settings(models.Model):

    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtp_server = models.CharField(blank=True, max_length=20)
    smtp_email = models.CharField(blank=True, max_length=20)
    smtp_password = models.CharField(blank=True, max_length=20)
    smtp_port = models.CharField(blank=True, max_length=20)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    about_us = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):

    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(blank=True, max_length=30)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'size': '40', 'class': 'input', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'size': '40', 'class': 'input', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'size': '40', 'class': 'input', 'placeholder': 'Email Address'}),
            'message': Textarea(attrs={'cols': 42, 'rows': 4, 'class': 'input', 'placeholder': 'Your Message'}),
        }


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.username

    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_image_tag(self):
        return mark_safe('<img src="{}" height = 50/>'.format(self.image.url))
    get_image_tag.description='Image'


class UserProfileFormu(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'country', 'image']