from django.shortcuts import render
from django.views import generic
from .models import CodePost
from django.db.models import Q
import operator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import pdb

from django.http import HttpResponse

from itertools import chain

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


class IndexView(generic.list.ListView):
    template_name = 'blog/index.html'
    content_object_name = "codeposts"
    model = CodePost
    # page = request.GET.get('page', 1)
    specialstyle = None

    def get_queryset(self):
        result = super(IndexView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            title = CodePost.objects.filter(title__icontains=query_list[0]).order_by('title');
            print("query: " + query_list[0])
            print("title: " + str(title))
            content = CodePost.objects.filter(content__icontains=query_list[0])
            print("content: " + str(content))
            content1 = CodePost.objects.filter()
            print("content1: " + str(content1))
            print(str(result))
            #result = list(chain(title, content))

            #pdb.set_trace()
            print("Title: " + str(title))
            print("Content: " + str(content))
            print("Got here!")
            print(result)
            result = title | content
            print("Result: " + str(result))
            print("Query: " + str(query_list[0]))
            return result

        return result

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["codeposts"] = CodePost.objects.all()
        context["results"] = self.get_queryset()
        context["codeposts"] = context["results"]
        codeposts = context["codeposts"]

        context["query"] = self.request.GET.get('q')

        #pdb.set_trace()
        page = self.request.GET.get('page')
        if not page:
            page = 1

        paginator = Paginator(codeposts, 5)
        try:
            codeposts = paginator.page(page)
        except PageNotAnInteger:
            codeposts = paginator.page(1)
        except EmptyPage:
            codeposts = paginator.page(paginator.num_pages)

        context["codeposts"] = codeposts
        print("Got here aswell!")
        print(str(context["results"]))
        return context
"""
    if request.GET.get("q"):
        self.specialstyle = request.GET.get("q")

    paginator = Paginator(codepost_list, 2)
    try:
        self.codeposts = paginator.page(page)
    except PageNotAnInteger:
        self.codeposts = paginator.page(1)
    except EmptyPage:
        self.codeposts = paginator.page(paginator.num_pages)
"""
    #return render(request, 'blog/index.html', {'codeposts': codeposts, 'specialstyle': specialstyle})


class BlogDetailView(generic.detail.DetailView):
    model = CodePost
    template_name = "blog/detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['now'] = "Right now this is the \"now\" variable"
        return context
