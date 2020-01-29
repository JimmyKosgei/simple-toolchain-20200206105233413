from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LabExamSerializer
from .models import LabExam
# Create your views here.


class LabExamView(viewsets.ModelViewSet):
    queryset = LabExam.objects.all()
    serializer_class = LabExamSerializer
