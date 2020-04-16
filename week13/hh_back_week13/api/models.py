from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    city = models.CharField(max_length=300)
    address = models.TextField(default='')

class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    salary = models.IntegerField(default='')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)


