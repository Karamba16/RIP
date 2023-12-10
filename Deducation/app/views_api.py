from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name']



class ApplicationForDeducationViewSet(viewsets.ModelViewSet):
    queryset = ApplicationForDeducation.objects.all()
    serializer_class = ApplicationForDeducationSerializer

    def create(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    @action(detail=True, methods=['put'])
    def confirm(self, request, pk=None):
        application = self.get_object()
        application.confirm()
        return Response({'status': 'confirmed'})