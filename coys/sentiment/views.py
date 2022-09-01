from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import scraper
from .models import *
from .forms import *

def entry(request):
    if request.method == 'POST':
        if "submit_postid" in request.POST:
            postForm = idForm(request.POST)
            if postForm.is_valid():
                print("Post ID form valid")
                postID = postForm.cleaned_data['postID']
                return HttpResponseRedirect('/sentiment/loadcomments/'+postID+'/')
        elif "submit_username" in request.POST:
            userForm = unameForm(request.POST)
            if userForm.is_valid():
                print("uname form valid")
                uname = userForm.cleaned_data['uname']
                return HttpResponseRedirect('/sentiment/user/'+uname+'/')
    else:
        postForm = idForm()
        userForm = unameForm()
    return render(request, 'sentiment/entry.html', {'postForm':postForm, 'userForm':userForm})

def loadcomments(request, id):
    scraper.loadPostByID(id)
    scraper.loadComments(id)
    p = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post=p).values()
    return render(request,'sentiment/loadcomments.html',context={'comments':comments})

def user(request, name):
    #TODO: add dates
    scraper.loadUserComments(name)
    u = User.objects.get(username=name)
    comments = Comment.objects.filter(author=name).values()
    return render(request, "sentiment/user.html",context={'comments':comments, 'name':name})
