from django.shortcuts import render
from django.http import HttpResponse

def say_hello_html(request):
  return HttpResponse('<h1>allo html!</h1>')

def say_hello(request):
  return render(request, 'hello.html', { 'name': 'Tsuki' })