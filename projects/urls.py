from django.conf.urls import url

from . import views

app_name = "projects"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<slug>[-_\w]+)/$', views.ProjectDetailView.as_view(), name="detail"),
]
