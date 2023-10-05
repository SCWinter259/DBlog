from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Article

# Create your views here.
# this is like an action creator

class Index(ListView):
    model = Article
    # get all the posts and show the newest first
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 1     # pagination