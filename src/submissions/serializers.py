from rest_framework import serializers

from submissions.models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['topic', 'text', 'patient']