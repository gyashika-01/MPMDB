from django.db import models
from django.db import connections 

# Create your models here.
class med_phytochem(models.Model):
    Plant_Name = models.TextField()
    Scientific_Name = models.TextField()
    Phytochemicals = models.TextField()
    Activity_Count = models.IntegerField()
    Formula = models.TextField()
    IUPAC_Name = models.TextField()
    SMILES = models.TextField()
    Plant_Part = models.TextField()
    Molecular_Mass = models.TextField()
    Monoisotopic_Mass = models.TextField()
    LogP = models.TextField()
    Hydrogen_Acceptors = models.TextField()
    Hydrogen_Donors = models.TextField()
    Rotatable_Bond_Count = models.TextField()
    Polar_Surface_Area = models.TextField()
    Structure = models.URLField()
    References = models.URLField()