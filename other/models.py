from django.db import models

# Create your models here.


class Participant(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    tel_nr = models.CharField(max_length=9)
    email = models.EmailField()
