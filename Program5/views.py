from django.shortcuts import render

def basic(request):
    return render(request,'basic.html')
