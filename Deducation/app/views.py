'''from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello world!')'''

from django.shortcuts import render, redirect
from django.db import connection
from django.urls import reverse
from django.db.models import Q
from app import models,serializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

'''def detailed_operations_page(request, id):
    data_by_id = db_operations.get('operations_to_perform')[id]
    return render(request, 'operation_types_detailed.html', {
        'operations_to_perform': data_by_id
    })
'''

def detailed_service_page(request, id):
    filtered_data=list(models.Student.objects.filter(student_id=id))[0]
    print(filtered_data)
    return render(request, 'operation_types_detailed.html',
        {'filtered_data': filtered_data})


def service_page(request):
    query = request.GET.get('q')

    if query:
        # Фильтрую данные, при этом учитываю поле "type"
        filtered_data =  list(models.Student.objects.filter(last_name__icontains=query))
        print(filtered_data)

    else:
        filtered_data = list(models.Student.objects.all())

        query = ""
        print(filtered_data)
    return render(request, "operation_types.html", {'filtered_data': filtered_data})
# Create your views here.



