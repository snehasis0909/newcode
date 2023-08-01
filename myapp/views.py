from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.


class CurdApi(viewsets.ViewSet):
    def addpost(self,request):
        payload = request.data
        siri = EmployeeSerializer(data=payload)
        if siri.is_valid():
            siri.save()
        return Response(siri.data,status=status.HTTP_200_OK)
    def get(self,request):
        data = Employee.objects.all().values()
        return Response(data,status=status.HTTP_200_OK)
    def deleterecords(self,request,id):
        qs = Employee.objects.filter(id = id)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
