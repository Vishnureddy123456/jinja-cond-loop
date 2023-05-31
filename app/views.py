from django.shortcuts import render

# Create your views here.
def nested(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'nested.html',d)
def forl(request):
    d={'name':'vishnu'}
    return render(request,'forl.html',d)
def ifelif(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'ifelif.html',d)