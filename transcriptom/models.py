from django.db import models
from django.db import connections 

# Create your models here.
class med_transcriptom(models.Model):
    Plant_Name = models.TextField()
    Scientific_Name = models.TextField(default="")
    SRA = models.TextField()
    DNA = models.TextField(default="")
    RNA = models.TextField(default="")
    BioProject = models.TextField()
    BioSample = models.TextField()
    NCBI_link = models.URLField()
