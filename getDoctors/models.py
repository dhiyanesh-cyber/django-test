from django.db import models

class Doctor(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    discipline = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'doctor_list'
