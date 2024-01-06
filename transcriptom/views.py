from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q
from .models import med_transcriptom

#transcriptom_view
class transcriptom_view(ListView):
    template_name= "transcriptom.html"

    def get_queryset(self):
        query = self.request.GET.get("q", default=".")
        object_list = med_transcriptom.objects.filter(Q(Plant_Name=query))
        return object_list
    