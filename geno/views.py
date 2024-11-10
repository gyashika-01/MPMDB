from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q
from .models import med_geno

#genome_view
class geno_view(ListView):
    template_name= "genomes.html"

    def get_queryset(self):
        query = self.request.GET.get("q", default=".")
        object_list = med_geno.objects.filter(Q(Plant_Name=query))
        return object_list

