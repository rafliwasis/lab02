from django.db import models        
from django.contrib.auth.models import User
from datetime import datetime                                            

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
