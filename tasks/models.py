from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=80)
    done = models.BooleanField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
