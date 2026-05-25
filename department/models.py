from django.db import models

class Department(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to='department_images/', null=True,blank=True)
    description=models.TextField()
    def __str__(self):
        return self.title