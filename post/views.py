import datetime

from django.shortcuts import HttpResponse, render


# Create your views here.

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, this is my project")


def current_date(request):
    if request.method == 'GET':
        return HttpResponse(f"{datetime.date.today()}")


def good_bye(request):
    if request.method == 'GET':
        return HttpResponse("Good bye user!")