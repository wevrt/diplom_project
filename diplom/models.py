from django.db import models

# Create your models here.
class Doctor(models.Model):
    name: models.CharField(max_length=200)

    class Meta:
        app_label = 'diplom'

    def __str__(self):
        return self.name
