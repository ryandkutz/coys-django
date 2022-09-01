from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import scraper
from .models import *
from .forms import *

def entry(request):
    if request.method == 'POST':
        form = idForm(request.POST)
        if form.is_valid():
            print("form valid")
            postID = form.cleaned_data['postID']
            scraper.loadPostByID(postID)
            scraper.loadComments(postID)
            p = Post.objects.get(pk=postID)
            comments = Comment.objects.filter(post=p).values()
            return render(request,'sentiment/loadcomments.html',context={'comments':comments})
    else:
        form = idForm()
    return render(request, 'sentiment/entry.html', {'form':form})
