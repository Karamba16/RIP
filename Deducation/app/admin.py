from django.contrib import admin
from .models import FacultyTypes,Users,ApplicationForDeducation
# Register your models here.
admin.site.register(FacultyTypes)
admin.site.register(Users)
admin.site.register(ApplicationForDeducation)