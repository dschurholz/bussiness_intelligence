from django.contrib import admin

from .models import Time


class TimeAdmin(admin.ModelAdmin):
    search_fields = ['id_date', 'ds_time']
    list_display = ('id_date', 'year', 'month', 'day',)

admin.site.register(Time, TimeAdmin)
