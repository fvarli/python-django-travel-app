from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from content.models import Category, Comment, Content, ContentForm

from home.models import UserProfile

from user.forms import UserUpdateForm, ProfileUpdateForm, AddNewTrip, AddNewCategory


@login_required(login_url='/login')
def index(request):
    category = Category.objects.all()
    current_user = request.user     # access user session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    #return HttpResponse(profile)
    context = {'category': category,
               'profile': profile}
    return render(request, 'user_profile.html', context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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
        return render(request, 'add_new_trip.html', context)\
    


@login_required(login_url='/login')
def add_new_category(request):
    if request.method == 'POST':
        new_category = AddNewCategory(request.POST, request.FILES)
        if new_category.is_valid():
            new_category.save()
            messages.success(request, 'Your new category has been added!')
            return redirect('/user')
    else:
        new_category = AddNewCategory()
        context = {
            'new_category': new_category
        }
        return render(request, 'add_new_category.html', context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def comments(request):
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {'comments': comments}
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def delete_comment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Your comment has been deleted.')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')
def contents(request):
    category = Category.objects.all()
    current_user = request.user
    contents = Content.objects.filter(user_id=current_user.id)
    context = {
        'contents': contents,
        'category': category
    }
    return render(request, 'contents.html', context)


@login_required(login_url='/login')
def add_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Content()
            data.user_id = current_user.id
            data.category = form.cleaned_data['category']
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            messages.success(request, 'Your trip has been added.')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Content Form Error: ', + str(form.errors))
            return HttpResponseRedirect('/user/add_content')
    else:
        form = ContentForm()
        context = {
            'form': form
        }
        return render(request, 'add_content.html', context)


@login_required(login_url='/login')
def edit_content(request, id):
    content = Content.objects.get(id=id)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your trip has been updated.')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Content Form Error: ', + str(form.errors))
            return HttpResponseRedirect('/user/edit_content/' + str(id))
    else:
        form = ContentForm(instance=content)
        context = {
            'form': form
        }
        return render(request, 'add_content.html', context)


@login_required(login_url='/login')
def delete_content(request, id):
    current_user = request.user
    Content.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Your trip has been deleted.')
    return HttpResponseRedirect('/user/contents')
