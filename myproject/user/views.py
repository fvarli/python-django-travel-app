from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from content.models import Category

from home.models import UserProfile

from user.forms import UserUpdateForm, ProfileUpdateForm, AddNewTrip


def index(request):
    category = Category.objects.all()
    current_user = request.user     # access user session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    #return HttpResponse(profile)
    context = {'category': category,
               'profile': profile}
    return render(request, 'user_profile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)     # request.user is user_data
        # "instance=request.user.user_profile" comes from "user_profile" model -> OneToOneField Relation
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')

    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)    # "user_profile" model -> OneToOneField Relation with user
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


# @login_required(login_url='/login')
def add_new_trip(request):
    if request.method == 'POST':
        new_trip = AddNewTrip(request.POST, request.FILES)
        if new_trip.is_valid():
            new_trip.save()
            messages.success(request, 'Your new trip has been added!')
            return redirect('/user')
    else:
        new_trip = AddNewTrip()
        context = {
            'new_trip': new_trip
        }
        return render(request, 'add_new_trip.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Important
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')

        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form,
            'category': category
        })
