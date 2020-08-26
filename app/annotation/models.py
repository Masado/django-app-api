import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Annotation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

