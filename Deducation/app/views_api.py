from rest_framework import viewsets
from .models import *
from .serializers import *


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ApplicationForDeducationViewSet(viewsets.ModelViewSet):
    queryset = ApplicationForDeducation.objects.all()
    serializer_class = ApplicationForDeducationSerializer
