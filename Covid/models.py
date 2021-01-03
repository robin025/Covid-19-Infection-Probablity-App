from django.db import models


# Create your models here.
class FormInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    fever_value = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    body_pain = models.IntegerField(default=0)
    runnyrose = models.IntegerField(default=0)
    diff_breath = models.IntegerField(default=0)
    coughprob = models.IntegerField(default=0)
    lososat = models.IntegerField(default=0)
    diabetic_patient = models.IntegerField(default=0)
    hypertension_prob = models.IntegerField(default=0)
    lung_disease = models.IntegerField(default=0)
    heart_disease = models.IntegerField(default=0)
    kidney_disease = models.IntegerField(default=0)

    def __str__(self):
        return self.name
