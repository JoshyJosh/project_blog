from django.shortcuts import render
from django.views import generic
from .models import CodePost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse

"""
# Create your views here.
def index(request):
    return HttpResponse("Soup!")
"""

"""
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'first_question'

    def get_queryset(self):
        Return first CodePost
        return CodePost.objects.first()
"""


def index(request):
    codepost_list = CodePost.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(codepost_list, 2)
    try:
        codeposts = paginator.page(page)
    except PageNotAnInteger:
        codeposts = paginator.page(1)
    except EmptyPage:
        codeposts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'codeposts': codeposts})
