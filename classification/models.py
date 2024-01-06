from django.db import models
from django.db import connections 
# Create your models here.

class med_class(models.Model):
    Plant_Id = models.IntegerField()
    Plant_Name =models.TextField()
    Scientific_Name = models.TextField()
    Kingdom = models.TextField()
    Division = models.TextField()
    Class = models.TextField()
    Order = models.TextField()
    Family = models.TextField()
    Genus = models.TextField()
    Species = models.TextField()
