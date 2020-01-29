from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('lab_exam', views.LabExamView)

urlpatterns = [
    path('', include(router.urls))
]
