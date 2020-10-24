from django.contrib import admin

# Register your models here.
from .models import Graph,Day

admin.site.register(Graph)
admin.site.register(Day)