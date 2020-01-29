from django.shortcuts import render
from rest_framework import viewsets
from .models import Diagnosis
from .serializers import DiagnosisSerializer

# Create your views here.
class DiagnosisView(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
