from django.shortcuts import render,redirect
from .serializers import CustomerSerializers
from .models import Customer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.response import Response


# Create your views here.

class ShowCustomerView(ListAPIView):
    serializer_class = CustomerSerializers
    model_serializers = Customer
    

class CreateCustomerView(CreateAPIView):
    serializer_class = CustomerSerializers
    model_serializers = Customer

class UpdateCustomerView(UpdateAPIView):
    serializer_class = CustomerSerializers
    model_serializers = Customer


class RetrieveCustomerView(RetrieveAPIView):
    serializer_class = CustomerSerializers
    model_serializers = Customer

class DestroyCustomerView(DestroyAPIView):
    serializer_class = CustomerSerializers
    model_serializers = Customer


def add_cust(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        
    template_name = 'app1/add_cust.html'
    context = {form : 'form'}
    return render(request,template_name,context)