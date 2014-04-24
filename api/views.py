from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import status

from core.models import Customer

from .serializers import CustomerSerializer


class CustomerList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all customers.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
