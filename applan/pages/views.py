
from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home_view(request,*args,**kwargs):
	print("h1")
	print(request.user)
	print("h2")
	#return HttpResponse("<h1> hello </h1>")
	return render(request,"home.html", {})


def contact_view(request,*args,**kwargs):
	return render(request,"contact.html", {})


def about_view(request,*args,**kwargs):
	my_context = {
		"my_number":123,
		"my_text" :"This is about me"
	}

	return render(request,"about.html",my_context)

