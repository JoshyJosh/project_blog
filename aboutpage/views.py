from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'aboutpage/index.html', {"title": "About page", "pagetype": "aboutpage"})
