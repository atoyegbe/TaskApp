import pytest
from mixer.backend.django import mixer
from django.urls import reverse

@pytest.mark.django_db
def test_tasks_list(client):
    url = reverse('viewtasks')
    response = client.get(url)
    
    assert response.status_code == 200
    

@pytest.mark.django_db
def test_tasks_detailed_data(client):
    tasks = mixer.blend('tasks.TaskApp', quantity=1)
    url = reverse('task', kwargs={'pk': tasks.pk})
    response = client.get(url)
    
    assert response.status_code == 200

@pytest.mark.django_db
def test_tasks_delete_url(client):
    tasks = mixer.blend('tasks.TaskApp', quantity=1)
    url = reverse('delete', kwargs={'pk': tasks.pk})
    
    response = client.get(url)
    
    assert response.status_code == 200