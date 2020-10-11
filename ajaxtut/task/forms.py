
from django import forms

from .models import Task



class TaskForm(forms.ModelForm):
	description = forms.CharField(
					required = False,
					widget=forms.Textarea(
						attrs = {
								"rows":5
						}
					  )
					)

	class Meta:
		model = Task 
		fields = (
			'title',
			'description',
			'length'
			)
		labels = {
			'length': ('Length (in hours)'),
		}
		help_texts = {
			'title': ("Name of Task."),
			'length': ("ex. .5 for half an hour"),
		}
class RawTaskForm(forms.Form):
	title = 	  forms.CharField()
	description = forms.CharField()
	length = 	  forms.CharField()