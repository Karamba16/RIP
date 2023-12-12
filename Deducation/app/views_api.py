from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .permissions import IsModerator
from .serializers import *

from django.conf import settings
import redis

session_storage = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name']


class ApplicationForDeducationViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsModerator()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.is_moderator:
            return ApplicationForDeducation.objects.all()
        return ApplicationForDeducation.objects.filter(user=self.request.user)

    serializer_class = ApplicationForDeducationSerializer

    def create(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    @action(detail=True, methods=['put'])
    def confirm(self, request, pk=None):
        application = self.get_object()
        application.confirm()
        return Response({'status': 'confirmed'})