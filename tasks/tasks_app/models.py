from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)


