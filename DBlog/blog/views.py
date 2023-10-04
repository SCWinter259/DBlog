from django.shortcuts import render
from django.views import View

# Create your views here.
# this is like an action creator

class Index(View):
    def get(self, request):
        return render(request, 'blog/index.html')