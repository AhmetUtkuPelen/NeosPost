from django.shortcuts import render
from .models import*

import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2024-03-29&'
       'sortBy=popularity&'
       'apiKey=bbd773aaa75649df8e65214bcc9b894d')

response = requests.get(url)

# Create your views here.

def index(request):
    context = {
        'news': response,
    }
    return render(request,'haberler/index.html', context=context)