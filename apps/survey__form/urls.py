from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^submission$', views.submission),
	url(r'^summary$', views.summary)
]