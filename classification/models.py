from django.db import models
from django.db import connections 
# Create your models here.

class med_class(models.Model):
    Plant_Name =models.TextField()
    Scientific_Name = models.TextField()
    NCBI_Taxonomy_ID = models.TextField()
    Order = models.TextField()
    Family = models.TextField()
    Genus = models.TextField()
    Species = models.TextField()
    NCBI_link = models.URLField(default = "")