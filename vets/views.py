from django.shortcuts import render
from .models import User
from .serializers import VetSerializer
from rest_framework import viewsets
# Create your views here.


class VetView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = VetSerializer
