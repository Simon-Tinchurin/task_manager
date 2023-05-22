from django.test import TestCase
from tasks_app.forms import TaskForm


class TestModels(TestCase):

    def test_task_form_valid(self):
        form = TaskForm(data={
            'title': 'Test Title',
            'content': 'Test Content'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_task_form_invalid(self):
        form = TaskForm(data={
            'title': '',
            'content': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
