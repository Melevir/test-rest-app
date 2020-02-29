from django.contrib.auth.models import User
from rest_framework import viewsets
from patients.serializers import UserSerializer, PatientSerializer
from patients.models import Patient


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
