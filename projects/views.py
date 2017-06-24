from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Project

from django.http import HttpResponse

# Create your views here.

"""
def index(request):
    return render(request, 'projects/index.html')
"""

class IndexView(generic.list.ListView):
    template_name = 'projects/index.html'
    content_object_name = "projects"
    model = Project
    # page = request.GET.get('page', 1)
    specialstyle = None

    def get_queryset(self):
        result = super(IndexView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            title = Project.objects.filter(title__icontains=query_list[0]).order_by('title');
            print("query: " + query_list[0])
            print("title: " + str(title))
            content = Project.objects.filter(content__icontains=query_list[0])
            print("content: " + str(content))
            content1 = Project.objects.filter()
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
        context["projects"] = Project.objects.all()
        context["results"] = self.get_queryset()
        context["projects"] = context["results"]
        projects = context["projects"]

        context["query"] = self.request.GET.get('q')

        #pdb.set_trace()
        page = self.request.GET.get('page')
        if not page:
            page = 1

        paginator = Paginator(projects, 5)
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)

        context["projects"] = projects

        context["title"] = "Projects page"
        print("Got here aswell!")
        print(str(context["results"]))
        return context

class ProjectDetailView(generic.detail.DetailView):
    model = Project
    template_name = "projects/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].title
        return context
