from django.db import models
from django.db import models

# Create your models here.
class Certificate(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    date = models.DateField()
    sign=models.CharField(max_length=100)
    # Add other fields as needed for your certificates

    def __str__(self):
        return self.name