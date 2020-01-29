from django.db import models
from cases.models import Case
from vets.models import User
# Create your models here.


class Diagnosis(models.Model):
    case_no = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='CASE_NO')
    vet_id = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=255, null=False)
    treatment = models.CharField(max_length=255, null=False)
    vet_remarks = models.CharField(max_length=255, null=True)
    revisit_date = models.DateField(null=True)
