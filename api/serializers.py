from rest_framework import serializers
from rest_framework.reverse import reverse

from .extensions.fields import ReverseField

from core.models import (Customer, DimReference, SpeedInfringement,
                         DimCustomerUnit)


class CustomerSerializer(serializers.ModelSerializer):
    url = ReverseField('api:customer-detail', args=('id_customer',))

    class Meta:
        model = Customer
        fields = ('url', 'id_customer', 'company', 'unit', 'ds_customer',)


class DimCustomerUnitSerializer(serializers.ModelSerializer):
    url = ReverseField('api:customer-unit-detail', args=('id',))

    class Meta:
        model = DimCustomerUnit
        fields = ('url', 'id', 'unit_plate', 'customer')


class DimReferenceSerializer(serializers.ModelSerializer):
    url = ReverseField('api:reference-detail', args=('id_reference',))

    class Meta:
        model = DimReference
        fields = ('url', 'id_reference', 'region', 'province',
                  'province_capital', 'district', 'road_type', 'road_name',
                  'road_block', 'poi_reference', 'poi_road', 'siege')


class SpeedInfringementSerializer(serializers.ModelSerializer):
    url = ReverseField('api:speed-infringement-detail', args=('id',))
    unit = ReverseField('api:customer-unit-detail', args=('unit.id',))
    reference = ReverseField('api:reference-detail',
                             args=('reference.id_reference',))

    class Meta:
        model = SpeedInfringement
        fields = ('url', 'id', 'date', 'speed', 'codemensa', 'unit',
                  'reference')
