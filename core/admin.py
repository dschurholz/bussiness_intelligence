from django.contrib import admin

from .models import (Customer, DimReference, DimCustomerUnit,
                     Event, Region, SpeedInfringement, Time, Cube, Graphics)


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['id_customer', 'ds_customer']
    list_display = ('id_customer', 'company', 'unit',)


class DimCustomerUnitAdmin(admin.ModelAdmin):
    search_fields = ['id', 'unit_plate']
    list_display = ('unit_plate', 'customer', 'id')


class DimReferenceAdmin(admin.ModelAdmin):
    search_fields = ['id_reference', 'region']
    list_display = ('region', 'province', 'district',
                    'road_name', 'id_reference')


class EventAdmin(admin.ModelAdmin):
    search_fields = ['time', 'total']
    list_display = ('time', 'region', 'customer',)


class RegionAdmin(admin.ModelAdmin):
    search_fields = ['id_region', 'via']
    list_display = ('id_region', 'city', 'province', 'district',)


class SpeedInfringementAdmin(admin.ModelAdmin):
    search_fields = ['id', 'unit']
    list_display = ('unit', 'date', 'speed', 'id')


class TimeAdmin(admin.ModelAdmin):
    search_fields = ['id_date', 'ds_time']
    list_display = ('id_date', 'year', 'month', 'day',)


class CubeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)


class GraphicsAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id_cube']
    list_display = ('name', 'ds_type',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(DimCustomerUnit, DimCustomerUnitAdmin)
admin.site.register(DimReference, DimReferenceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(SpeedInfringement, SpeedInfringementAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Cube, CubeAdmin)
admin.site.register(Graphics, GraphicsAdmin)
