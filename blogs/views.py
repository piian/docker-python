# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'blogs/index')


def blog(request):
    return None
