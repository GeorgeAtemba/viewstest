from django.db import models

# Create your models here.
class MixMod(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    work = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name