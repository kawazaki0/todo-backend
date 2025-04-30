from django.db import models


class Task(models.Model):
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.BooleanField()

    @property
    def full_name(self):
        return f"{self.surname} {self.first_name}"
