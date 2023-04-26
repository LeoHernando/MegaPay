from django.db import models

# Create your models here.

class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cellphone_number = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    notified_at = models.DateTimeField(auto_now_add=True)
    claimed_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'api'

class Payouts(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    invoice = models.CharField(max_length=100)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notified_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'api'