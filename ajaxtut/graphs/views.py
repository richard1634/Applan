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


