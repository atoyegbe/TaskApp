import pytest
from mixer.backend.django import mixer
from django.urls import reverse
from django.test import RequestFactory
from tasks.views import *
from tasks.models import TaskApp
from datetime import datetime

@pytest.mark.django_db
class TestViews:
    
    def test_home_page(self):
        url = reverse('home')
        request = RequestFactory().get(url)
        response = home(request)
        
        assert response.status_code == 200
    
    def test_view_tasks(self):
        my_tasks = mixer.blend(TaskApp, title="Me")
        
        url = reverse("viewtasks")
        request = RequestFactory().get(url)
        response =  viewTasks(request)
        
        assert response.status_code == 200
        
    def test_task_view(self):
        task = TaskApp.objects.create(title='First pytest', description="Testing my task app", is_complete=False, date_created=datetime.now())

        url = reverse('task', kwargs={'pk': task.pk})
        request = RequestFactory().get(url)
        
        response = taskView(request, pk=task.pk)
        assert response.status_code == 200
        