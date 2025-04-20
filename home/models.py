from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    tasktitle=models.CharField(max_length=70)
    taskdesc=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.tasktitle
