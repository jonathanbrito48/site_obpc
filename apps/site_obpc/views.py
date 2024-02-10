from django.shortcuts import render

def index(request):
    return render(request,'site/index.html')

def pastores(request):
    return render(request,'site/pastores.html')

def umasbrac(request):
    return render(request,'site/umasbrac.html')

def ufebrac(request):
    return render(request,'site/ufebrac.html')