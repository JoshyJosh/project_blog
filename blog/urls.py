from django.conf.urls import url

from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^blog/(?P<slug>[-_\w]+)/$', views.BlogDetailView.as_view(), name="detail"),
]
