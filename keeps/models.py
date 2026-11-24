from django.db import models
from django.utils import timezone
import datetime


class Tag(models.Model):
    tag_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.tag_text


class Note(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.note_text