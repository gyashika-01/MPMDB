from django.db import models
from django.db import connections 

# Create your models here.
class med_transcriptom(models.Model):
    Plant_Name = models.TextField()
    Biosample = models.TextField()
    Bioproject = models.TextField()
    SRA = models.TextField()
    NCBI_link = models.URLField()
