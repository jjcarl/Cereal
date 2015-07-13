# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cereal.manufacturer'
        db.add_column(u'main_cereal', 'manufacturer',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.CerealMaker'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cereal.manufacturer'
        db.delete_column(u'main_cereal', 'manufacturer_id')


    models = {
        u'main.cereal': {
            'Meta': {'object_name': 'Cereal'},
            'calories': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'carbs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cups_per_serving': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fiber': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.CerealMaker']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'potassium': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'protein': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'serving_size_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shelf': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sodium': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sugars': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vitamins': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'main.cerealmaker': {
            'Meta': {'object_name': 'CerealMaker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']