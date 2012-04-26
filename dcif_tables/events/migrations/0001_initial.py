# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Table'
        db.create_table('events_table', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('table', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('events', ['Table'])

    def backwards(self, orm):
        # Deleting model 'Table'
        db.delete_table('events_table')

    models = {
        'events.table': {
            'Meta': {'object_name': 'Table'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'table': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['events']