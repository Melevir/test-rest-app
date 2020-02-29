from django.db import models


class Submission(models.Model):
    topic = models.CharField(max_length=512)
    text = models.TextField()

    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
