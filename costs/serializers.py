from rest_framework import serializers
from .models import Cost

class CostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = ('case_no', 'vet_id', 'drugs', 'lab_test',
                  'proff_fees', 'mileage', 'other_charges', 'total_charges', 'paid', 'balance')
