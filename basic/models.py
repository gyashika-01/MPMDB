from django.db import models
from django.db import connections 

# Create your models here.
class med_basic(models.Model):
    Plant_Id = models.IntegerField()
    Plant_Name = models.CharField(max_length=100)
    Description = models.TextField()
    Parts_Used = models.TextField()
    Weather_Conditions_Required_to_Grow = models.TextField()
    Bioactive_Compound = models.TextField()
    Chemical_Properties = models.TextField()
    Morphological_Features = models.TextField()
    Medicinal_Value = models.TextField()
    States_of_India_Support_their_Growth = models.TextField()
    References = models.URLField()