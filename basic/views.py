from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q
from .models import med_basic

#basic_view
class basic_view(ListView):
    template_name= "basic.html"

    def get_queryset(self):
        query = self.request.GET.get("q", default=".")
        object_list = med_basic.objects.filter(Q(Plant_Name=query))
        return object_list