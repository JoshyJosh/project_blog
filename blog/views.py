from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse

"""
# Create your views here.
def index(request):
    return HttpResponse("Soup!")
"""


class IndexView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return
