from django.db import models
from django.db import connections 

# Create your models here.
class med_proteom(models.Model):
    Plant_Name = models.TextField()
    Protein = models.TextField()
    Protein_Identical_Group = models.TextField()
    NCBI_link = models.URLField()



    