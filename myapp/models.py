from django.db import models

# Create your models here.


class Employee(models.Model):
    ename = models.CharField(max_length=100, null=True,blank=True)
    company = models.CharField(max_length=100,null=True, blank=True)
    esal = models.IntegerField(null=True,blank=True)
    class Meta:
        db_table ='Employee'
