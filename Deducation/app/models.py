from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)

    #class Meta:
     #   managed = False
      #  db_table = 'student'


class ApplicationForDeducation(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user')
    date_application_create = models.DateField(blank=True, null=True)
    date_application_accept = models.DateField(blank=True, null=True)
    date_application_complete = models.DateField(blank=True, null=True)
    application_status = models.TextField()  # This field type is a guess.

    students = models.ManyToManyField(Student)

    #class Meta:
     #   managed = False
      #  db_table = 'application_for_deducation'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.CharField(unique=True, max_length=30, blank=True, null=True)
    login = models.CharField(unique=True, max_length=40, blank=True, null=True)
    password = models.CharField(unique=True, max_length=30, blank=True, null=True)
    role = models.CharField(blank=True, null=True)

    #class Meta:
     #   managed = False
      #  db_table = 'users'


class FacultyTypes(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=30)
    faculty_description = models.CharField(max_length=1500)
    faculty_image_url = models.CharField(max_length=50, blank=True, null=True)
    faculty_status = models.TextField()  # This field type is a guess.
    def __str__(self):
        return self.faculty_name

    """
    class Meta:
        managed = False
        db_table = 'faculty_types'
    """