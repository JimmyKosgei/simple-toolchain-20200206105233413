from django.shortcuts import render
from rest_framework import viewsets
from .models import Cost
from .serializers import CostsSerializer

# Create your views here.


class CostView(viewsets.ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostsSerializer
