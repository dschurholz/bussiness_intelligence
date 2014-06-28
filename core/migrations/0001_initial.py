# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table('cliente', (
            ('id_customer', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='id_cliente')),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='empresa')),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='unidad')),
            ('ds_customer', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, db_column='ds_cliente')),
        ))
        db.send_create_signal(u'core', ['Customer'])

        # Adding model 'DimReference'
        db.create_table('dimreferenciasdw', (
            ('id_reference', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idReferencia')),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=110, null=True, db_column='sDpto')),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, db_column='sProvi')),
            ('province_capital', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, db_column='sCapProvi')),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, db_column='sDistr')),
            ('road_type', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, db_column='sTipVia')),
            ('road_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, db_column='sNomVia')),
            ('road_block', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, db_column='sCuadVia')),
            ('poi_reference', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, db_column='sPoiRef')),
            ('poi_road', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, db_column='sPoiVia')),
            ('siege', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, db_column='sCerco')),
        ))
        db.send_create_signal(u'core', ['DimReference'])

        # Adding model 'DimCustomerUnit'
        db.create_table('dimunidadclientedw', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='UNI_CODIGO')),
            ('unit_plate', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, db_column='UNI_MATRICULA')),
            ('customer', self.gf('django.db.models.fields.CharField')(max_length=160, null=True, db_column='CLI_NOMBRE')),
        ))
        db.send_create_signal(u'core', ['DimCustomerUnit'])

        # Adding model 'Region'
        db.create_table('region', (
            ('id_region', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='Ciudad')),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='Provincia')),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='Distrito')),
            ('road', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, db_column='Via')),
        ))
        db.send_create_signal(u'core', ['Region'])

        # Adding model 'Time'
        db.create_table('tiempo', (
            ('id_date', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='Anho')),
            ('month', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='Mes')),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='Dia')),
            ('ds_time', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='ds_tiempo')),
        ))
        db.send_create_signal(u'core', ['Time'])

        # Adding model 'SpeedInfringement'
        db.create_table('factexcesovelocidad', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.DimCustomerUnit'], db_column='UNI_CODIGODW')),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, db_column='MEC_FECCOMUNDW')),
            ('speed', self.gf('django.db.models.fields.SmallIntegerField')(null=True, db_column='MEC_VELOCIDAD')),
            ('reference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.DimReference'], db_column='idReferencia')),
            ('codemensa', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='MEC_CODMENSA')),
            ('id_date', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Time'], null=True)),
        ))
        db.send_create_signal(u'core', ['SpeedInfringement'])

        # Adding model 'Event'
        db.create_table('hechos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Time'], null=True, db_column='id_tiempo')),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Region'], null=True, db_column='id_region')),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Customer'], null=True, db_column='id_cliente')),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='cantidad')),
        ))
        db.send_create_signal(u'core', ['Event'])

        # Adding model 'Cube'
        db.create_table(u'core_cube', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'core', ['Cube'])

        # Adding model 'Dimention'
        db.create_table(u'core_dimention', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('table_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cube', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Cube'])),
        ))
        db.send_create_signal(u'core', ['Dimention'])

        # Adding model 'Hierarchy'
        db.create_table(u'core_hierarchy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('columne_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dimention', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Dimention'])),
        ))
        db.send_create_signal(u'core', ['Hierarchy'])

        # Adding model 'Graphics'
        db.create_table(u'core_graphics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ds_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id_cube', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Cube'], null=True)),
        ))
        db.send_create_signal(u'core', ['Graphics'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table('cliente')

        # Deleting model 'DimReference'
        db.delete_table('dimreferenciasdw')

        # Deleting model 'DimCustomerUnit'
        db.delete_table('dimunidadclientedw')

        # Deleting model 'Region'
        db.delete_table('region')

        # Deleting model 'Time'
        db.delete_table('tiempo')

        # Deleting model 'SpeedInfringement'
        db.delete_table('factexcesovelocidad')

        # Deleting model 'Event'
        db.delete_table('hechos')

        # Deleting model 'Cube'
        db.delete_table(u'core_cube')

        # Deleting model 'Dimention'
        db.delete_table(u'core_dimention')

        # Deleting model 'Hierarchy'
        db.delete_table(u'core_hierarchy')

        # Deleting model 'Graphics'
        db.delete_table(u'core_graphics')


    models = {
        u'core.cube': {
            'Meta': {'ordering': "['name']", 'object_name': 'Cube'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.customer': {
            'Meta': {'ordering': "['id_customer']", 'object_name': 'Customer', 'db_table': "'cliente'"},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'empresa'"}),
            'ds_customer': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'db_column': "'ds_cliente'"}),
            'id_customer': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'id_cliente'"}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'unidad'"})
        },
        u'core.dimcustomerunit': {
            'Meta': {'ordering': "['customer']", 'object_name': 'DimCustomerUnit', 'db_table': "'dimunidadclientedw'"},
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '160', 'null': 'True', 'db_column': "'CLI_NOMBRE'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'UNI_CODIGO'"}),
            'unit_plate': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'db_column': "'UNI_MATRICULA'"})
        },
        u'core.dimention': {
            'Meta': {'ordering': "['name']", 'object_name': 'Dimention'},
            'cube': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Cube']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'table_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.dimreference': {
            'Meta': {'ordering': "['region']", 'object_name': 'DimReference', 'db_table': "'dimreferenciasdw'"},
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'sDistr'"}),
            'id_reference': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idReferencia'"}),
            'poi_reference': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'sPoiRef'"}),
            'poi_road': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'sPoiVia'"}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'sProvi'"}),
            'province_capital': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'sCapProvi'"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '110', 'null': 'True', 'db_column': "'sDpto'"}),
            'road_block': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'db_column': "'sCuadVia'"}),
            'road_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'sNomVia'"}),
            'road_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "'sTipVia'"}),
            'siege': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'sCerco'"})
        },
        u'core.event': {
            'Meta': {'ordering': "['time', 'region', 'customer', 'total']", 'object_name': 'Event', 'db_table': "'hechos'"},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Customer']", 'null': 'True', 'db_column': "'id_cliente'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Region']", 'null': 'True', 'db_column': "'id_region'"}),
            'time': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Time']", 'null': 'True', 'db_column': "'id_tiempo'"}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'cantidad'"})
        },
        u'core.graphics': {
            'Meta': {'ordering': "['name', 'ds_type', 'id_cube']", 'object_name': 'Graphics'},
            'ds_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_cube': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Cube']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.hierarchy': {
            'Meta': {'ordering': "['name']", 'object_name': 'Hierarchy'},
            'columne_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dimention': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Dimention']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.region': {
            'Meta': {'ordering': "['id_region']", 'object_name': 'Region', 'db_table': "'region'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'Ciudad'"}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'Distrito'"}),
            'id_region': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'Provincia'"}),
            'road': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_column': "'Via'"})
        },
        u'core.speedinfringement': {
            'Meta': {'ordering': "['id']", 'object_name': 'SpeedInfringement', 'db_table': "'factexcesovelocidad'"},
            'codemensa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'MEC_CODMENSA'"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'MEC_FECCOMUNDW'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'id_date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Time']", 'null': 'True'}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DimReference']", 'db_column': "'idReferencia'"}),
            'speed': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'db_column': "'MEC_VELOCIDAD'"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DimCustomerUnit']", 'db_column': "'UNI_CODIGODW'"})
        },
        u'core.time': {
            'Meta': {'ordering': "['id_date']", 'object_name': 'Time', 'db_table': "'tiempo'"},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'Dia'"}),
            'ds_time': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'ds_tiempo'"}),
            'id_date': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'Mes'"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'Anho'"})
        }
    }

    complete_apps = ['core']