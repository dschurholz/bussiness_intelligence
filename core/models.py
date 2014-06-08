from django.db import models


class Customer(models.Model):
    id_customer = models.IntegerField(primary_key=True, db_column='id_cliente')
    company = models.CharField(max_length=50, db_column='empresa', null=True)
    unit = models.CharField(max_length=50, db_column='unidad', null=True)
    ds_customer = models.CharField(max_length=10, db_column='ds_cliente',
                                   null=True)

    class Meta:
        db_table = 'cliente'
        ordering = ['id_customer']

    def __unicode__(self):
        return "%s-%s" % (self.company, self.unit)


class DimReference(models.Model):
    id_reference = models.IntegerField(primary_key=True,
                                       db_column='idReferencia')
    region = models.CharField(max_length=110, db_column='sDpto', null=True)
    province = models.CharField(max_length=100, db_column='sProvi', null=True)
    province_capital = models.CharField(max_length=100, db_column='sCapProvi',
                                        null=True)
    district = models.CharField(max_length=100, db_column='sDistr', null=True)
    road_type = models.CharField(max_length=2, db_column='sTipVia', null=True)
    road_name = models.CharField(max_length=100, db_column='sNomVia',
                                 null=True)
    road_block = models.CharField(max_length=10, db_column='sCuadVia',
                                  null=True)
    poi_reference = models.CharField(max_length=100, db_column='sPoiRef',
                                     null=True)
    poi_road = models.CharField(max_length=100, db_column='sPoiVia', null=True)
    siege = models.CharField(max_length=100, db_column='sCerco', null=True)

    class Meta:
        db_table = 'dimreferenciasdw'
        ordering = ['region']

    def __unicode__(self):
        return "%s-%s-%s-%s" % (self.id_reference, self.region, self.province,
                                self.district)


class DimCustomerUnit(models.Model):
    id = models.IntegerField(primary_key=True, db_column='UNI_CODIGO')
    unit_plate = models.CharField(max_length=9, db_column='UNI_MATRICULA',
                                  null=True)
    customer = models.CharField(max_length=160, db_column='CLI_NOMBRE',
                                null=True)

    class Meta:
        db_table = 'dimunidadclientedw'
        ordering = ['customer']

    def __unicode__(self):
        return "%s-%s" % (self.unit_plate, self.customer)


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=50, db_column='Ciudad', null=True)
    province = models.CharField(max_length=50, db_column='Provincia',
                                null=True)
    district = models.CharField(max_length=50, db_column='Distrito', null=True)
    road = models.CharField(max_length=50, db_column='Via', null=True)

    class Meta:
        db_table = 'region'
        ordering = ['id_region']

    def __unicode__(self):
        return "%s-%s-%s" % (self.city, self.province, self.district)


class SpeedInfringement(models.Model):
    id = models.IntegerField(primary_key=True)
    unit = models.ForeignKey(DimCustomerUnit, db_column='UNI_CODIGODW')
    date = models.DateField(db_column='MEC_FECCOMUNDW', null=True)
    speed = models.SmallIntegerField(db_column='MEC_VELOCIDAD', null=True)
    reference = models.ForeignKey(DimReference, db_column='idReferencia')
    codemensa = models.IntegerField(db_column='MEC_CODMENSA', null=True)

    class Meta:
        db_table = 'factexcesovelocidad'
        ordering = ['id']


class Time(models.Model):
    id_date = models.IntegerField(primary_key=True)
    year = models.CharField(max_length=50, db_column='Anho')
    month = models.CharField(max_length=50, db_column='Mes')
    day = models.CharField(max_length=50, db_column='Dia')
    ds_time = models.CharField(max_length=50, db_column='ds_tiempo')

    class Meta:
        db_table = 'tiempo'
        ordering = ['id_date']

    def __unicode__(self):
        return "%s-%s-%s" % (self.year, self.month, self.day)


class Event(models.Model):
    time = models.ForeignKey(Time, db_column='id_tiempo', null=True)
    region = models.ForeignKey(Region, db_column='id_region', null=True)
    customer = models.ForeignKey(Customer, db_column='id_cliente', null=True)
    total = models.IntegerField(db_column='cantidad', null=True)

    class Meta:
        db_table = 'hechos'
        ordering = ['time', 'region', 'customer', 'total']


class Cube(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']


class Dimention(models.Model):
    name = models.CharField(max_length=50, unique=True)
    table_name = models.CharField(max_length=100)
    cube = models.ForeignKey(Cube)

    class Meta:
        ordering = ['name']


class Hierarchy(models.Model):
    name = models.CharField(max_length=50, unique=True)
    columne_name = models.CharField(max_length=100)
    dimention = models.ForeignKey(Dimention)

    class Meta:
        ordering = ['name']


class Graphics(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ds_type = models.CharField(max_length=50)
    id_cube = models.ForeignKey(Cube, null=True)

    class Meta:
        ordering = ['name', 'ds_type', 'id_cube']
