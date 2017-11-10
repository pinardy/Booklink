from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    # template = loader.get_template('booklist/index.html')
    return render(request, 'booklist/index.html', {})
    # return HttpResponse("<h1> test </h1>")

def work(request):
    # template = loader.get_template('booklist/index.html')
    return render(request, 'booklist/work.html', {})
    # return HttpResponse("<h1> test </h1>")