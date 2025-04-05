from django.db import models
from django.db import connections 

# Create your models here.
class med_proteom(models.Model):
    Plant_Name = models.TextField()
    Scientific_Name = models.TextField(default="")
    Protein_Seq = models.TextField(default="")
    Identical_Protein_Groups = models.TextField()
    Protein = models.TextField()
    NCBI_link = models.URLField()



    