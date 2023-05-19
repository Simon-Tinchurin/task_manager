from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)


