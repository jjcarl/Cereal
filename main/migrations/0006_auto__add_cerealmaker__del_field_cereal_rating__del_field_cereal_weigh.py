# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CerealMaker'
        db.create_table(u'main_cerealmaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['CerealMaker'])

        # Deleting field 'Cereal.rating'
        db.delete_column(u'main_cereal', 'rating')

        # Deleting field 'Cereal.weight'
        db.delete_column(u'main_cereal', 'weight')

        # Deleting field 'Cereal.mfr'
        db.delete_column(u'main_cereal', 'mfr')

        # Deleting field 'Cereal.cups'
        db.delete_column(u'main_cereal', 'cups')

        # Adding field 'Cereal.serving_size_weight'
        db.add_column(u'main_cereal', 'serving_size_weight',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cereal.cups_per_serving'
        db.add_column(u'main_cereal', 'cups_per_serving',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'CerealMaker'
        db.delete_table(u'main_cerealmaker')

        # Adding field 'Cereal.rating'
        db.add_column(u'main_cereal', 'rating',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cereal.weight'
        db.add_column(u'main_cereal', 'weight',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cereal.mfr'
        db.add_column(u'main_cereal', 'mfr',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cereal.cups'
        db.add_column(u'main_cereal', 'cups',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Cereal.serving_size_weight'
        db.delete_column(u'main_cereal', 'serving_size_weight')

        # Deleting field 'Cereal.cups_per_serving'
        db.delete_column(u'main_cereal', 'cups_per_serving')


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