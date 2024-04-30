from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def skills(request):
    return render(request, 'skills.html')

def ask(request):
    return render(request,'ask.html')