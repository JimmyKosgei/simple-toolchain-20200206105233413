from django.db import models
from cases.models import Case
from vets.models import User


class Cost(models.Model):
    case_no = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='CASE_NO')
    vet_id = models.ForeignKey(User, on_delete=models.CASCADE)
    drugs = models.IntegerField(null=False)
    lab_test = models.IntegerField(null=False)
    proff_fees = models.IntegerField(null=False)
    mileage = models.IntegerField(null=False)
    other_charges = models.IntegerField(null=False)
    total_charges = models.IntegerField(null=False)
    paid = models.IntegerField(null=False)
    balance = models.IntegerField(null=False)
