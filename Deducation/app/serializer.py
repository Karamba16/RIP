from rest_framework import serializers

from app.models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "email",
            "login",
            "password",
        ]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ApplicationForDeducationSerializer(serializers.ModelSerializer):
    #user = UsersSerializer(role='1',read_only=True)

    class Meta:
        model = ApplicationForDeducation
        fields = [
            "application_id",
            "user",
            "date_application_create",
            "date_application_accept",
            "date_application_complete",
            "application_status",
            "moderator_id",
        ]

class ApplicationDetailed(serializers.ModelSerializer):
    #user = UsersSerializer(role='1', read_only=True)
    class Meta:
        model = ApplicationForDeducation
        fields = '__all__'