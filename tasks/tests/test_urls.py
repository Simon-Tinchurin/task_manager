from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from tasks_app.views import log_in, user_tasks, register, log_out


# to run this test - python manage.py test tests.test_urls
class TestUrl(SimpleTestCase):
    databases = {'default'}

    def set_up(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_login(self):
        url = reverse('')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(resolve(url).func, log_in)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_page(self):
        url = reverse('tasks')
        data = {'title': 'Test Task',
                'content': 'Content'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(resolve(url).func, user_tasks)

    def test_register_page(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(resolve(url).func, register)
        self.assertTemplateUsed(response, 'register.html')

    def test_log_out(self):
        url = reverse('log_out')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse(''))
        self.assertEquals(resolve(url).func, log_out)
        self.assertFalse('_auth_user_id' in self.client.session)
