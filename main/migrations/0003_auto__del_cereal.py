# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Cereal'
        db.delete_table(u'main_cereal')


    def backwards(self, orm):
        # Adding model 'Cereal'
        db.create_table(u'main_cereal', (
            ('rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('fiber', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('sodium', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('shelf', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sugars', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('calories', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('potass', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mfr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('protein', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cups', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vitamins', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Cereal'])


    models = {
        
    }

    complete_apps = ['main']