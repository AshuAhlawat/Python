from django.db import models

# Create your models here.

class Note(models.Model):
    
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    urgency = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title