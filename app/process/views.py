import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from app.process.models import Process

def tela(request):

    process = Process.objects.all()
    
    first = Process.objects.first()


    data = {
        "valor":1000,
        "objs":process,
        "primeiro":first,
        
    }

    return render(
        request,
        "home.html",
        data,
    )

