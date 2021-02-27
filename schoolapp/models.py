from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    board =  models.CharField(max_length=50)
    location =  models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School , on_delete=models.CASCADE)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name