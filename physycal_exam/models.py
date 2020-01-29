from django.db import models
from cases.models import Case
from vets.models import User


class PhysicalExam(models.Model):
    case_no = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='CASE_NO')
    vet_id = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.CharField(max_length=255)
    respiration_rate = models.CharField(max_length=255, null=True)
    heart_rate = models.CharField(max_length=255, null=True)
    respiration_rate = models.CharField(max_length=255, null=True)
    mucus_membrane = models.CharField(max_length=255, null=True)
    crt = models.CharField(max_length=255, null=True)
    rumen_mot = models.CharField(max_length=255, null=True)
    temperament = models.CharField(max_length=255, null=True)
    appetite = models.CharField(max_length=255, null=True)
    gait = models.CharField(max_length=255, null=True)
    body_condition = models.CharField(max_length=255, null=True)
    hydration = models.CharField(max_length=255, null=True)
    other_observations = models.CharField(max_length=255, null=True)
    samples_taken = models.CharField(max_length=255, null=True)
    tentative_dx = models.CharField(max_length=255)
