from django.db import models
from django.db import connections 

# Create your models here.
class med_genomes(models.Model):
    Plant_Id = models.IntegerField()
    Plant_Name = models.TextField()
    Chromosome_Number = models.TextField()
    Ploidy = models.TextField()
    Genome_Size = models.TextField()
    Nucleotide = models.TextField()
    mRNA_Sequence = models.TextField()
    Genome_Sequence = models.TextField()
    NCBI_link = models.URLField()
    Literature_Paper_Link = models.URLField()