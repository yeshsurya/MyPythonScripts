from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
	return HttpResponse("Welcome to the tutorial.")

# Create your views here.
