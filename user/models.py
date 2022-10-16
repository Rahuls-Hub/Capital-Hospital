from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Appointment1(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor.name + "--" + self.patient.name


class Register(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.IntegerField(null=True)

    def __str__(self):
        return self.name


