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

class GameSave(models.Model):
    seed=models.CharField(max_length=30)
    nick=models.CharField(max_length=30)
    posX=models.FloatField()
    posY=models.FloatField()
    inventory=models.CharField(max_length=100)
    currentLevel=models.IntegerField()
    rooms_passed=models.CharField(max_length=500)
    score=models.IntegerField()
    run_time=models.DateTimeField(default=datetime.now())
