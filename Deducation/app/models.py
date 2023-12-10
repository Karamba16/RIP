from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    description = models.CharField(max_length=1500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=[('1', '1'), ('2', '2')], default='1')

    def __str__(self):
        return self.first_name


class ApplicationForDeducation(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user')
    date_application_create = models.DateField(blank=True, null=True)
    date_application_accept = models.DateField(blank=True, null=True)
    date_application_complete = models.DateField(blank=True, null=True)
    application_status = models.TextField()  # This field type is a guess.

    def confirm(self):
        self.application_status = 'confirmed'
        self.save()

    students = models.ManyToManyField(Student)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.CharField(unique=True, max_length=30, blank=True, null=True)
    login = models.CharField(unique=True, max_length=40, blank=True, null=True)
    password = models.CharField(unique=True, max_length=30, blank=True, null=True)
    role = models.CharField(max_length=30, choices=[('1', '1'), ('2', '2')], default='1')




