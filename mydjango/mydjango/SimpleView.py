from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   return HttpResponse("Hello, world!")
def htmlpage(request):
    return render(request,'index.html')