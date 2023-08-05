from django.shortcuts import render
from rest_framework.views import APIView
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CustomerView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serialiser = CustomerSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data,status=status.HTTP_201_CREATED)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request,pk,format=None):
        customer=Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        customer=Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        customer=Customer.objects.get(pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



