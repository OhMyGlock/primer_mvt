from django.db import models

class Familiares(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    birth = models.DateField()
    date = models.DateTimeField(auto_now_add=True)