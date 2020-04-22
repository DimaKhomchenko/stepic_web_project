from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

def test(request, *args, **kwargs):
	return HttpResponse('OK')

#def not_found(request):
#	return HttpResponseNotFound
