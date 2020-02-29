import datetime

from django.contrib.auth import get_user_model
from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    birth_date = models.DateField()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    @property
    def age(self):
        today = datetime.date.today()
        return (
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
