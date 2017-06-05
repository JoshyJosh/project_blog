from django.conf.urls import url

from . import views

app_name = "aboutpage"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'post/(?P<contentpost_slug>)^$', views.DetailView.as_view(), name="detail"),
]
