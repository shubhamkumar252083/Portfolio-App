from django.db import models

# Create your models here.


class ContactMe(models.Model):
    name = models.CharField(max_length=120)  # max_length = required
    email = models.EmailField(
        max_length=120, blank=False, null=False, unique=True)
    ph_no = models.IntegerField(
        blank=False, null=False, unique=True)
    msg = models.TextField(blank=True, null=True)
