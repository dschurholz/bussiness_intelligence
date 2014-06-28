# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SpeedInfringement.ref_date'
        db.add_column('factexcesovelocidad', 'ref_date',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Time'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SpeedInfringement.id_date'
        db.add_column('factexcesovelocidad', 'id_date',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Time'], null=True),
                      keep_default=False)


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
            'ref_date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Time']", 'null': 'True'}),
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