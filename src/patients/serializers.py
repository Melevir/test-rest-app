from django.contrib.auth.models import User
from rest_framework import serializers

from patients.models import Patient


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'age', 'user']
