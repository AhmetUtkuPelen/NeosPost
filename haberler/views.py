from django.shortcuts import render
from .models import*
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='bbd773aaa75649df8e65214bcc9b894d')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

# Create your views here.

def index(request):

    context = {
        
    }
    
    return render(request,'haberler/index.html')