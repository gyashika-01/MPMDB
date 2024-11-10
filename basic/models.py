from django.db import models
from django.db import connections 

# Create your models here.
class med_basic(models.Model):
    Plant_Name = models.TextField()
    Scientific_Name = models.TextField()
    Description = models.TextField()
    Parts_Used = models.TextField()
    Weather_Conditions_Required_to_Grow = models.TextField()
    Chemical_Properties = models.TextField()
    Morphological_Features = models.TextField()
    Medicinal_Value = models.TextField()
    Worldwide_regions_Support_their_Growth = models.TextField()
    References = models.URLField()