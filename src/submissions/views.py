from rest_framework import viewsets
from submissions.serializers import SubmissionSerializer
from submissions.models import Submission


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
