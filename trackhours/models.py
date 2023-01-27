import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class WorkDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=15, null=True, blank=True, )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    delta_time = models.CharField(max_length=5, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.start_time >= self.end_time:
            raise ValueError("EndTime Error")
        if self.end_time - self.start_time > datetime.timedelta(hours=16):
            raise ValueError("To much time")
        else:
            self.delta_time = self.end_time - self.start_time
            self.day = str(f'{self.start_time.strftime("%A-%d-%m")}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.day





class SendReport(models.Model):
    start_day = models.DateField()
    end_date = models.DateField()
    email = models.CharField(max_length=250)

    def __str__(self):
        return self.email
