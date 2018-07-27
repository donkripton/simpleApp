from django.conf.urls import url, include

from dataStorage import views

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^list/$', views.list, name='list'),
	url(r'^add/$', views.add, name='add'),
]


