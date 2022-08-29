from django.shortcuts import render
from django.http import HttpResponse
from . import scraper

def index(request):
    return HttpResponse("test")
def sent(request):
    scraper.loadPostByID("x0vl1m")
    scraper.loadComments("x0vl1m")
    return HttpResponse("sent")
