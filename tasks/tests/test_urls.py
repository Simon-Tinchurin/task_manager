from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tasks_app.views import log_in, user_tasks, register, log_out


class TestUrl(SimpleTestCase):

    def test_main(self):
        url = reverse('')
        self.assertEquals(resolve(url).func, log_in)

    def test_user_page(self):
        url = reverse('tasks')
        self.assertEquals(resolve(url).func, user_tasks)

    def test_register_page(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_log_out(self):
        url = reverse('log_out')
        self.assertEquals(resolve(url).func, log_out)
