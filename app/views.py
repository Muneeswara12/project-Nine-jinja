from django.shortcuts import render

# Create your views here.
def hero(request):
    d={'a':10,'b':20}
    return render(request,'hero.html',context=d)