from django.shortcuts import render
from .models import PhysicalExam
from .serializers import PhysicalExamSerializer
from rest_framework import viewsets
# Create your views here.


class PhysicalExamView(viewsets.ModelViewSet):
    queryset = PhysicalExam.objects.all()
    serializer_class = PhysicalExamSerializer
