from django.db import models
from django.db import connections 

# Create your models here.
class med_metabolites(models.Model):
    Plant_Id = models.IntegerField()
    Plant_Name = models.TextField()
    General_Metabolites = models.TextField()
    Primary_Metabolites_and_Functions = models.TextField()
    Secondary_Metabolites_and_Functions = models.TextField()
    Unique_Metabolites = models.TextField()
    Metabolic_Pathway = models.TextField()
    Structure_of_Metabolites_1 = models.URLField()
    Structure_of_Metabolites_2 = models.URLField()
    References = models.URLField()
    kegg_link = models.URLField()