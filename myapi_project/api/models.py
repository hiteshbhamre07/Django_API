from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    role = models.IntegerField()
    city = models.CharField(max_length=10)

    def __str__(self):
        return self.name