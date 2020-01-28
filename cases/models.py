from django.db import models


class Case(models.Model):
    clinician_name = models.CharField(null=True, max_length=30)
    date_reported = models.DateTimeField(null=False)
    date_attended = models.DateTimeField(null=False)
    owner = models.CharField(null=False, max_length=255)
    contact = models.CharField(null=False, max_length=255)
    address = models.CharField(null=False, max_length=255)
    species = models.CharField(null=False, max_length=255)
    breed = models.CharField(null=False, max_length=255)
    sex = models.CharField(null=False, max_length=255)
    age = models.CharField(null=False, max_length=255)
    identity = models.CharField(null=False, max_length=255)
    complaint = models.CharField(null=False, max_length=255),
