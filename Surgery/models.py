from django.db import models

# Create your models here.
class SurgeryInfo(models.Models):
    name_patient = models.CharacterField(max_length=200)
    location_patient = models.CharacterField(max_length=200)
    date_opened = models.DateField(null=true, blank=true)