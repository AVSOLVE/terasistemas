import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from app.process.models import *


def tela(request):
    process = Process.objects.all()[:10]

    first = Process.objects.first()

    em_analise = Process.objects.filter(client_status="OPERAÇÃO CONCLUÍDA").count()

    data = {
        "valor": 1000,
        "objs": process,
        "primeiro": first,
        "client_count": Client.objects.count(),
        "em_analise": em_analise,
    }

    return render(
        request,
        "home.html",
        data,
    )
