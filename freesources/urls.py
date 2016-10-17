from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^feedback/(?P<fd_type>[A-Za-z0-9-_]+)/(?P<event_id>[0-9]+)/$', views.feedback, name='feedback'),	
]
