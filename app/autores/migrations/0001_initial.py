# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Autor'
        db.create_table(u'autores_autor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'autores', ['Autor'])

        # Adding model 'Invitado'
        db.create_table(u'autores_invitado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'autores', ['Invitado'])


    def backwards(self, orm):
        # Deleting model 'Autor'
        db.delete_table(u'autores_autor')

        # Deleting model 'Invitado'
        db.delete_table(u'autores_invitado')


    models = {
        u'autores.autor': {
            'Meta': {'object_name': 'Autor'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'autores.invitado': {
            'Meta': {'object_name': 'Invitado'},
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['autores']