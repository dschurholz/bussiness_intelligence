from rest_framework import serializers
from rest_framework.reverse import reverse

from core.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id_customer', 'company', 'unit', 'ds_customer',)
