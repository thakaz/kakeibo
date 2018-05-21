from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World,You're at the app index")

#from django.shortcuts import render

# Create your views here.
