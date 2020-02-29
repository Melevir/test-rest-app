from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from patients.models import Patient
from submissions.models import Submission


class Command(BaseCommand):
    def handle(self, *args, **options):
        patients_amount = 3
        submissions_amount = 5

        fake = Faker()
        User = get_user_model()

        user = User.objects.create(email=fake.ascii_company_email(), username=fake.user_name())
        for _ in range(patients_amount):
            Patient.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(),
                user=user,
            )
        for _ in range(submissions_amount):
            Submission.objects.create(
                topic=fake.sentence(),
                text=fake.text(),
                patient=Patient.objects.order_by('?').first(),
            )
