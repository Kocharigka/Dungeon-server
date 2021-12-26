from django.db import models
from  datetime import date,datetime
# Create your models here.
from django.utils.timezone import now

class Runs(models.Model):
    seed=models.CharField(max_length=30)
    run_date=models.DateField(default=now())

class Leaderbord(models.Model):
    seed=models.ForeignKey(Runs,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    score=models.IntegerField()