from django.db import models

# Create your models here.

class Health_Metrics(models.Model):
   # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='health_metrics')
    recorded_at = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    blood_pressure_systolic = models.IntegerField(blank=True, null=True)
    blood_pressure_diastolic = models.IntegerField(blank=True, null=True)
    body_temperature = models.FloatField(blank=True, null=True)
    heart_rate = models.IntegerField(blank=True, null=True)
    respiratory_rate = models.IntegerField(blank=True, null=True)
    blood_glucose_levels = models.FloatField(blank=True, null=True)
    cholesterol_total = models.FloatField(blank=True, null=True)
    cholesterol_hdl = models.FloatField(blank=True, null=True)
    cholesterol_ldl = models.FloatField(blank=True, null=True)
    cholesterol_triglycerides = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Health Metrics for {self.patient} at {self.recorded_at}"
