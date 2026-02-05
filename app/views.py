from django.shortcuts import render
from .models import Caterer

def home(request):
    caterers = Caterer.objects.all()
    return render(request, "index.html", {
        "caterers": caterers
    })
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')