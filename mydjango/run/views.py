from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return render(request,'index.html')
# #     # return render(request, 'index.html'),

def bootstrap(request):
    return render(request,'bootstrap.html')