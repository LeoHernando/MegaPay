from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import EmployeesSerializer, PayoutsSerializer
from api.models import Employees, Payouts


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class PayoutsViewSet(viewsets.ModelViewSet):
    queryset = Payouts.objects.all()
    serializer_class = PayoutsSerializer

