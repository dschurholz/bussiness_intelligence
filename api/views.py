from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import status

from core.models import (Customer, DimCustomerUnit, DimReference,
                         SpeedInfringement)

from .serializers import (CustomerSerializer, SpeedInfringementSerializer,
                          DimCustomerUnitSerializer, DimReferenceSerializer)


class CustomerList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all customers.

    `POST`: Add a new customer.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail of a customers.

    `PUT`: Updates customer information.

    `DELETE`: Deletes Customer.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pk_url_kwarg = 'customer_id'


class DimCustomerUnitList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all customer units.

    `POST`: Add a customer unit.
    """

    queryset = DimCustomerUnit.objects.all()
    serializer_class = DimCustomerUnitSerializer


class DimCustomerUnitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a customer unit.

    `PUT`: Updates a customer unit's information.

    `DELETE`: Deletes a customer unit.
    """

    queryset = DimCustomerUnit.objects.all()
    serializer_class = DimCustomerUnitSerializer
    pk_url_kwarg = 'unit_id'


class DimReferenceList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all references.

    `POST`: Add a reference.
    """

    queryset = DimReference.objects.all()
    serializer_class = DimReferenceSerializer


class DimReferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a reference.

    `PUT`: Updates a reference.

    `DELETE`: Deletes a reference.
    """

    queryset = DimReference.objects.all()
    serializer_class = DimReferenceSerializer
    pk_url_kwarg = 'ref_id'


class SpeedInfringementList(generics.ListCreateAPIView):
    """
    `GET`: Returns a list of all speed infringements.

    `POST`: Add a speed infringement.
    """

    queryset = SpeedInfringement.objects.all()
    serializer_class = SpeedInfringementSerializer


class SpeedInfringementDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    `GET`: Returns detail about a speed infringement.

    `PUT`: Updates speed infringement information.

    `DELETE`: Deletes speed infringement.
    """

    queryset = SpeedInfringement.objects.all()
    serializer_class = SpeedInfringementSerializer
    pk_url_kwarg = 'spinf_id'