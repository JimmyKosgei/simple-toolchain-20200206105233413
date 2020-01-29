from rest_framework import serializers
from .models import Diagnosis

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('case_no', 'vet_id', 'diagnosis', 'treatment', 'vet_remarks', 'revisit_date')
