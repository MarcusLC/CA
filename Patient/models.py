from django.db import models

class PatientInfo(models.Models):
    patient_name = models.CharacterField(max_length=200)
    date_of_birth = models.DateField(null=true, blank=true)
    surgery_info = models.ForeignKey(surgery_app)
