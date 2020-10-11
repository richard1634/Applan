from django.shortcuts import render
from .models import Task
# Create your views here.
from .forms import TaskForm
from django.shortcuts import redirect
from django.http import HttpResponse

def task_create_view(request):
    my_form = TaskForm()
    if request.method == "POST":
        my_form = TaskForm(request.POST)
        if my_form.is_valid():
            my_form = my_form.save(commit=False)
            my_form.user = request.user ##save the user as they make task
            my_form.save()
            return redirect('/create')
    #########PULL WHATEVER IS CONNECTED TO MY ID##################
    obj = Task.objects.filter(user = request.user)
    context = {
        "form":my_form,
        "object_list": obj
    }

    return render(request,"tasks/task_create.html",context)

def task_delete_view(request,id):
    obj = Task.objects.get(id = id)
    if request.method == 'POST':
        obj.delete()
      #  return HttpResponse('<script>history.back();</script>')
        return redirect('/create')
    #return render(request,"tasks/task_create.html")

 
# def task_detail_view(request):
#     obj = Task.objects.get(id=3)
#     context = {
#     'title': obj.title,
#     'description': obj.description
#     }
#     return render(request,"tasks/task.html",{})