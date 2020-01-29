from django.db import models
from cases.models import Case
from vets.models import User
# Create your models here.


class LabExam(models.Model):
    case_no = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='CASE_NO')
    vet_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tests_done = models.CharField(max_length=255)
    test_results = models.CharField(max_length=255)
    lab_dx = models.CharField(max_length=255, null=True)
