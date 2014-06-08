from rest_framework import serializers
from rest_framework.reverse import reverse

from .extensions.fields import ReverseField

from core.models import (Customer, DimReference, SpeedInfringement,
                         DimCustomerUnit, Region, Time, Event, Cube, Graphics,
                         Dimention, Hierarchy)


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


class RegionSerializer(serializers.ModelSerializer):
    url = ReverseField('api:region-detail', args=('id_region',))

    class Meta:
        model = Region
        fields = ('url', 'id_region', 'city', 'province', 'district', 'road')


class TimeSerializer(serializers.ModelSerializer):
    url = ReverseField('api:time-detail', args=('id_date',))

    class Meta:
        model = Time
        fields = ('url', 'id_date', 'year', 'month', 'day', 'ds_time')


class EventSerializer(serializers.ModelSerializer):
    url = ReverseField('api:event-detail', args=('total',))
    time = ReverseField('api:event-time-detail', args=('id_tiempo',))
    region = ReverseField('api:event-region-detail', args=('id_region',))
    customer = ReverseField('api:event-customer-detail', args=('id_cliente',))

    class Meta:
        model = Event
        fields = ('url', 'time', 'region', 'customer', 'total')


class CubeSerializer(serializers.ModelSerializer):
    url = ReverseField('api:cube-detail', args=('id',))

    class Meta:
        model = Cube
        fields = ('id', 'name')


class DimentionSerializer(serializers.ModelSerializer):
    url = ReverseField('api:dimention-detail', args=('id',))
    cube = ReverseField('api:cube-detail', args=('cube',))

    class Meta:
        model = Dimention
        fields = ('id', 'name', 'table_name')


class HierarchySerializer(serializers.ModelSerializer):
    url = ReverseField('api:hierarchy-detail', args=('id',))
    dimention = ReverseField('api:dimention-detail', args=('dimention',))

    class Meta:
        model = Hierarchy
        fields = ('id', 'name', 'columne_name')


class GraphicsSerializer(serializers.ModelSerializer):
    url = ReverseField('api:graphics-detail', args=('id',))
    cube = ReverseField('api:cube-detail', args=('id_cube',))

    class Meta:
        model = Graphics
        fields = ('id', 'name', 'ds_type')
