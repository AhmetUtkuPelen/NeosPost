from django.shortcuts import render
from .models import*

# Create your views here.

def index(request):
    return render(request,'haberler/index.html')