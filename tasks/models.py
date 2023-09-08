from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=80)
    done = models.BooleanField()
    date = models.DateField()
    time = models.TimeField()

    def __int__(self):
        return self.id


class UserTask(models.Model):
    user = models.IntegerField()
    task = models.IntegerField()

    def __int__(self):
        return self.id
