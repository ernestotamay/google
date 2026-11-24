from django.db import models

class List(models.Model):
    list = models.CharField(max_length=20)

    def __str__(self):
        return self.list


class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
    task = models.CharField(max_length=20)
    detail = models.CharField(max_length=250)
    repeat = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.task
