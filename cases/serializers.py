from rest_framework import serializers
from .models import Case

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('case_no', 'vet_id', 'clinician_name',
                  'date_reported', 'date_attended', 'owner', 'contact', 'address', 'species', 'breed', 'sex', 'age', 'identity', 'complaint')
