from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from content.models import CommentForm, Comment


def index(request):
    return HttpResponse("Project Page")


@login_required(login_url='/login')

def add_comment(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST':    # if form is posted
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user     # access user session informaton

            data = Comment()
            data.user_id = current_user.id
            data.content_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')   # client computer ip address
            data.save()     # save it to database

            messages.success(request, "Your comment has been sent. Thank you!")
            return HttpResponseRedirect(url)

    messages.warning(request, 'Your comment has not been sent. Please check and send it again')
    return HttpResponseRedirect(url)
