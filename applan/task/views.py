from django.shortcuts import render
from .models import Task
# Create your views here.



def task_create_view(request):
	print(request.GET)
	print(request.POST)
	title = request.POST.get('title')
	print(title)
	context = {}
	return render(request,"tasks/task_create.html",context)

def task_detail_view(request):
	obj = Task.objects.get(id=1)
	context = {
	'title': obj.title,
	'description': obj.description
	}
	return render(request,"tasks/task.html",context)