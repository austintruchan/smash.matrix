from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('smashtournament/index.html')
	context = RequestContext(request)	
	return HttpResponse(template.render(context)) 

def leaders(request):
	template = loader.get_template('smashtournament/leaders.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

def match(request):
	template = loader.get_template('smashtournament/match.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))

