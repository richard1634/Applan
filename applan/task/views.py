from django.shortcuts import render
from .models import Task
# Create your views here.



# def task_create_view(request):
# 	form 

def task_detail_view(request):
	obj = Task.objects.get(id=1)
	context = {
	'title': obj.title,
	'description': obj.description
	}
	return render(request,"detail.html",context)