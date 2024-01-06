from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
def home_view(request, *args, **kwargs):
    return render (request, "home.html", {})

def intro_view(request, *args, **kwargs):
    return render (request, "intro.html", {})

def aloevera_view(request, *args, **kwargs):
    return render (request, "aloevera.html", {})

def amla_view(request, *args, **kwargs):
    return render (request, "amla.html", {})

def ashwagandha_view(request, *args, **kwargs):
    return render (request, "ashwagandha.html", {})

def babool_view(request, *args, **kwargs):
    return render (request, "babool.html", {})

def bhringraj_view(request, *args, **kwargs):
    return render (request, "bhringraj.html", {})

def cinnamon_view(request, *args, **kwargs):
    return render (request, "cinnamon.html", {})

def clove_view(request, *args, **kwargs):
    return render (request, "clove.html", {})

def cumin_view(request, *args, **kwargs):
    return render (request, "cumin.html", {})

def curry_view(request, *args, **kwargs):
    return render (request, "curry.html", {})

def eucalyptus_view(request, *args, **kwargs):
    return render (request, "eucalyptus.html", {})

def ginger_view(request, *args, **kwargs):
    return render (request, "ginger.html", {})

def lavender_view(request, *args, **kwargs):
    return render (request, "lavender.html", {})

def mehndi_view(request, *args, **kwargs):
    return render (request, "mehndi.html", {})

def neem_view(request, *args, **kwargs):
    return render (request, "neem.html", {})

def peppermint_view(request, *args, **kwargs):
    return render (request, "peppermint.html", {})

def tulsi_view(request, *args, **kwargs):
    return render (request, "tulsi.html", {})

def turmeric_view(request, *args, **kwargs):
    return render (request, "turmeric.html", {})