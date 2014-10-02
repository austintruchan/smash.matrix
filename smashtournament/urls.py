from django.conf.urls import patterns, url

from smashtournament import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^leaders/', views.leaders, name='leaders'),
	url(r'^match/', views.match, name='match'),
)
