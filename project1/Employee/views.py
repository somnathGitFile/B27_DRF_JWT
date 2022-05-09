from django.shortcuts import render
from .models import Employee
from Employee.serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
# Create your views here.

class EmployeeInfo(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    authentication_classes =[JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated,]