import pytest
from django.urls import reverse
from django.test import RequestFactory
from tasks.forms import TaskForm

@pytest.mark.parametrize("title, description, validity",
                         [('First form','Testing form with pytest parameter', True ),
                          ('Second form','Testing form using pytest', True ),])
def test_form_data(title, description, validity):
    form = TaskForm(data={
        'title': title,
        'description': description,
    })
    
    assert form.is_valid() is validity