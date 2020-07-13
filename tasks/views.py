from django.shortcuts import render, redirect
from .forms import TaskForm 
from .models import *
# Create your views here.
def home(request):
	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect("home")

	template_name = "index.html"
	return render(request, template_name, context={'form': form})


def viewTasks(request):
	all_tasks = TaskApp.objects.all()
	template_name="tasks.html"

	return render(request, template_name, context={'all_tasks': all_tasks})

def taskView(request, pk):
	task = TaskApp.objects.get(id=pk)

	template_name = 'task.html'
	context = {'task': task}
	return render(request, template_name, context)

def deleteTask(request, pk):

	task_d = TaskApp.objects.get(id=pk)

	if request.method == 'POST':
		task_d.delete()
		return redirect('viewtasks')

	template_name='delete.html'
	context = {'task_d': task_d}

	return render(request, template_name, context)

