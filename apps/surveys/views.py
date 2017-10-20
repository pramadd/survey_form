from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
       request.session['count'] = 0
    return render(request,'surveys/index.html')

def process(request):
    number=get_random_string(length=14)
    request.session['number']=number
    request.session['count'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request,'surveys/result.html')

def refresh(request):
  return redirect('/')
