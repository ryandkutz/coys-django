from django.shortcuts import render
from django.http import HttpResponse
from . import scraper

def index(request):
    return HttpResponse("test")
def sent(request):
    scraper.loadPost()
    return HttpResponse("sent")
