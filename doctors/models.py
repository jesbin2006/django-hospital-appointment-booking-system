from django.db import models
from department.models import Department

class Doctors(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor_images/', null=True,blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='doctors')
    specialization=models.CharField(max_length=200)
    experience=models.FloatField()
    history=models.TextField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name