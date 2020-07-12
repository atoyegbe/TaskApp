
from django.urls import path, include

from .views import *
urlpatterns = [
	path('', home, name='home'),
	path('tasks/', viewTasks, name="viewtasks"),

	path('task/<str:pk>', taskView, name="task"),
	path('delete/<str:pk>', deleteTask, name="delete")
]
