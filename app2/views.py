from django.shortcuts import render

# Create your views here.

# def Admin(request):
#     return render(request,'adminmainpage.html')

# def Admlog(request):
#     return render(request,'admlogin.html')

def Admhome(request):
    return render(request,'adminhome.html')

def Admup(request):
    return render(request,'adminupload.html')

def Userpro(request):
    return render(request,'userprofiles.html')
