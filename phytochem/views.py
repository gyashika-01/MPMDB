from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q
from .models import med_phytochem

class phytochem_view(ListView):
    template_name= "metabolites.html"

    def get_queryset(self):
        query = self.request.GET.get("q", default=".")
        object_list = med_phytochem.objects.filter(Q(Phytochemicals=query))
        return object_list
