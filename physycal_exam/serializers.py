from .models import PhysicalExam
from rest_framework import serializers

class PhysicalExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalExam
        fields = ('case_no', 'vet_id', 'temperature',
                  'respiration_rate', 'heart_rate', 'mucus_membrane', 'crt', 'rumen_mot', 'temperature', 'appetite', 'gait', 'body_condition', 'hydration', 'other_observations', 'samples_taken', 'tentative_dx')
