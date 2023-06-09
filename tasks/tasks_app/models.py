from django.db import models
from django.contrib.auth.models import User


# task model with one-to-many relationship
class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
