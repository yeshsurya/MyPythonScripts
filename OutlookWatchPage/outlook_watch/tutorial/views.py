from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from tutorial.authhelper import get_signin_url

def home(request):
	#redirect_uri = request.build_absolute_uri(reverse('tutorial:gettoken'))
    #sign_in_url = get_signin_url(redirect_uri)
    #return HttpResponse('<a href="' + sign_in_url +'">Click here to sign in and view your mail</a>')
	sign_in_url='#'
	context = { 'siginin_url' : sign_in_url }
	return render(request,'tutorial/home.html',context)
# Create your views here.
def gettoken(request):
  return HttpResponse('gettoken view')