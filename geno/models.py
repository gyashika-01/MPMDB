from django.db import models
from django.db import connections 

# Create your models here.
class med_geno(models.Model):
    Plant_Name = models.TextField()
    Scientific_Name = models.TextField()
    Nucleotide = models.TextField()
    Genome_Sequence = models.TextField()
    mRNA_Sequence = models.TextField()
    NCBI_link = models.URLField()