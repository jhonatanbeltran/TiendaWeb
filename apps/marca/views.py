from django.shortcuts import render
from .models import marca
# Create your views here.

def inicio(request):
    return render(request, 'index.html')