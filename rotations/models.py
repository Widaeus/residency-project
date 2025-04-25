from django.db import models
from django.contrib.auth.models import User

class Rotation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date   = models.DateField()

    def __str__(self):
        return f"{self.service}: {self.start_date} → {self.end_date}"

    @property
    def months(self):
        dy = self.end_date.year - self.start_date.year
        dm = self.end_date.month - self.start_date.month
        return dy * 12 + dm