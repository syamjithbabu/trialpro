from django.shortcuts import render

# Create your views here.

def Hey(request):
    return render(request,'htmlpage.html')

def Log(request):
    return render(request,'loginpage.html')

def Sign(request):
    return render(request,'signup.html')

def Home(request):
    return render(request,'homepage.html')

def Pay(request):
    return render(request,'payment.html')    
    

