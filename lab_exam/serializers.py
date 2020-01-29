from rest_framework import serializers
from .models import LabExam
class LabExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabExam
        fields = ('case_no', 'vet_id', 'tests_done', 'test_results', 'lab_dx')
