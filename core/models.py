from django.db import models


class Time(models.Model):
    id_date = models.IntegerField(primary_key=True)
    year = models.CharField(max_length=50, db_column='Anho')
    month = models.CharField(max_length=50, db_column='Mes')
    day = models.CharField(max_length=50, db_column='Dia')
    ds_time = models.CharField(max_length=50, db_column='ds_tiempo')

    class Meta:
        db_table = 'tiempo'
        ordering = ['id_date']
