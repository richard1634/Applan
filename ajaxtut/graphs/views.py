from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
# Views.py
from django.views.generic import ListView
from .models import Graph
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.

class GraphView(ListView):
    model = Graph
    template_name = 'graphs/graphs.html'
    context_object_name = 'my_graph'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

        
def graph_view(request,*args,**kwargs):
    graph = Graph.objects.get(user=request.user)
    #return HttpResponse("<h1> hello </h1>")
    # print(graph.days)
    # print(graph.days[0])
    my_date = []
    my_efficiency = []
    # for day,percent in graph.days:
    #     my_date.append(day)
    #     my_efficiency.append(percent)
    for item in graph.days:
        my_tuple = eval(item)
        my_date.append(my_tuple[0])
        my_efficiency.append(my_tuple[1])
    date_efficiency_zip = zip(my_date,my_efficiency)
    print(my_date)
    my_context = {
    	"my_date": my_date,
    	"my_efficiency": my_efficiency,
        "my_zip" : date_efficiency_zip
    }
    return render(request,'graphs/graphs.html', my_context)



# def graph_view(request,*args,**kwargs):

#     return render(request,'graphs/graphs.html')