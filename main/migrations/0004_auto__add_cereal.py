# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cereal'
        db.create_table(u'main_cereal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('mfr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('calories', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('protein', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sodium', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fiber', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('carbs', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('sugars', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('potass', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('vitamins', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('shelf', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cups', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Cereal'])


    def backwards(self, orm):
        # Deleting model 'Cereal'
        db.delete_table(u'main_cereal')


    models = {
        u'main.cereal': {
            'Meta': {'object_name': 'Cereal'},
            'calories': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'carbs': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cups': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fiber': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mfr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'potass': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'protein': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shelf': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sodium': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sugars': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vitamins': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']