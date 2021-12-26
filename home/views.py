from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home.html")

def yoga(request):
    return render(request,"yoga.html")

def sc(request):
    return render(request,"sc.html")    