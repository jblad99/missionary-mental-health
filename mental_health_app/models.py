# mental_health_app/models.py
from django.db import models

class Missionary(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Response(models.Model):
    missionary = models.ForeignKey(Missionary, on_delete=models.CASCADE)
    mission_president_comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)