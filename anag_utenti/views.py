from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<center><html><head><img src='logo_agricontable_workinprogress.png' ></head></html></center>")
