from django.shortcuts import render

# Create your views here.
# Views.py
from django.views.generic import ListView
from .models import CrudUser, Task2
from django.views.generic import View
from django.http import JsonResponse

class CrudView(ListView):
    model = Task2
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)



class CreateCrudUser(View):
    def get(self, request):
        name1 = request.GET.get('title', None)
        address1 = request.GET.get('description', None)
        age1 = request.GET.get('length', None)

        timer_in_secs = int(age1) * 60
        obj = Task2.objects.create(
            user = request.user,
            title = name1,
            description = address1,
            length = age1,
            timer = timer_in_secs
        )

        task2 = {'id':obj.id,'title':obj.title,'description':obj.description,'length':obj.length}

        data = {
            'task2': task2
        }
        return JsonResponse(data)



class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)
        timer_in_secs = int(age1) * 60
        
        obj = Task2.objects.get(id=id1)
        obj.title = name1
        obj.description = address1
        obj.length = age1
        obj.timer = timer_in_secs
        obj.save()

        task2 = {'id':obj.id,'title':obj.title,'description':obj.description,'length':obj.length}

        data = {
            'task2': task2
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Task2.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class TimeCrudUser(View):
    #return id and timer
    def get(self,request):
        id1 = request.GET.get('id',None)
        obj = Task2.objects.get(id=id1)
        data = {'id':obj.id,'timer':obj.timer}
        return JsonResponse(data)


class PauseCrudUser(View):
    def get(self,request):
        time_left1 = request.GET.get('time_left', None)

        id1 = request.GET.get('id',None)
        try:
            idx = time_left1.index(":")
            timer1 = time_left1[:idx]
            seconds1 = time_left1[idx+1:]

            obj = Task2.objects.get(id=id1)
            obj.timer = (int(timer1) * 60) + int(seconds1)
            obj.save()

            my_id = obj.id
            data = {
                'paused': True,
                'id' : my_id
            }
            return JsonResponse(data)
        except ValueError:
            data = {
                'paused': False,
            }
            return JsonResponse(data)


class CalcCrudUser(View):
    def get(self,request):
        mylist = Task2.objects.filter(user=self.request.user)
        completed = 0
        total = 0
        for task in mylist:
            completed += task.timer/60
            total += float(task.length)

        efficiency = 1 - (completed/total)
        data = {
            'efficiency':round(efficiency * 100,2),
        }
        return JsonResponse(data)


class ResetAllTimersCrudUser(View):
    def get(self,request):
        mylist = Task2.objects.filter(user=self.request.user)
        id_arr = []
        for task in mylist:
            task.timer = int(task.length) * 60
            id_arr.append(task.id)
            task.save()
        data = {
            'reset':True,
            'id_arr':id_arr,
        }
        return JsonResponse(data)


        #return all id's of all tasks -> make them all timer again -> stop all intervals