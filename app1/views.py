from django.shortcuts import render

# Create your views here.

def Hey(request):
    return render(request,'htmlpage.html')

def Log(request):
    return render(request,'loginpage.html')

