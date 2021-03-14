from django.db import models

# Create your models here.
class Novel(models.Model):
    
    user = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user