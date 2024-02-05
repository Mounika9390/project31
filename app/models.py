from django.db import models

# Create your models here.
class Company(models.Model):
    cname=models.CharField(max_length=100)
    cmanager=models.CharField(max_length=100)
    clocation=models.CharField(max_length=100)
    email=models.EmailField(default='mouni@gmail.com')
    reenteremail=models.EmailField(default='mouni@gmail.com')

    def __str__(self):
        return self.cname