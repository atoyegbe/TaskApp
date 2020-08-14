from mixer.backend.django import mixer
import pytest
from tasks.models import TaskApp
from datetime import datetime
@pytest.mark.django_db
class TestModels:
    
    def test_task_app_str(self):
        task = TaskApp.objects.create(title='First pytest', description="Testing my task app", is_complete=False, date_created=datetime.now())
        assert task.title == 'First pytest'
        assert str(task) == 'First pytest'