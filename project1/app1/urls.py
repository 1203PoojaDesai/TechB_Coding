from django.urls import path
from .views import ShowCustomerView,CreateCustomerView,DestroyCustomerView,UpdateCustomerView,RetrieveCustomerView,add_cust

urlpatterns = [
    path('acv/',CreateCustomerView.as_view()),
    path('scv/',ShowCustomerView.as_view()),
    path('dcv/',DestroyCustomerView.as_view()),
    path('ucv/',UpdateCustomerView.as_view()),
    path('rcv',RetrieveCustomerView.as_view()),
    path('ccv/',add_cust)
]
