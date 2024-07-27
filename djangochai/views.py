from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'website\index.html')

def about(request):
    return render(request,'website/about.html')
    # return HttpResponse("about")

def contact(request):
    return render(request,'website\contact.html')
    # return HttpResponse("contact")

