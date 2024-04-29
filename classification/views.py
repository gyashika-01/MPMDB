from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q
from .models import med_class

#classification_view
class classification_view(ListView):
    template_name= "classification.html"

    def get_queryset(self):
        query = self.request.GET.get("q", default=".")
        query0 = self.request.GET.get("p", default=".")
        object_list = med_class.objects.filter(Q(Plant_Name__icontains=query), Q(Genus__icontains = query0))
        return object_list