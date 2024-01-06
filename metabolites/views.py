from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q
from .models import med_metabolites

class metabolites_view(ListView):
    template_name= "metabolites.html"

    def get_queryset(self):
        query = self.request.GET.get("q", default=".")
        object_list = med_metabolites.objects.filter(Q(Plant_Name=query))
        return object_list