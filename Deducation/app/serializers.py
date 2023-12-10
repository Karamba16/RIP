from .models import *
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ApplicationForDeducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForDeducation
        fields = '__all__'