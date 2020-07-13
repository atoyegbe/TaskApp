from django.forms import ModelForm
from .models import TaskApp


class TaskForm(ModelForm):
	class Meta:
		model = TaskApp
		fields = ['title', 'description']


    