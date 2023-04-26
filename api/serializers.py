from rest_framework import serializers
from api.models import Employees, Payouts

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class PayoutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payouts
        fields = '__all__'