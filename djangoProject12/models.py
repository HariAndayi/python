from django.db import models


class student(models.Model):
    name= models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    number = models.IntegerField(blank=False, null=False)

def __str__(self):
    return self.name