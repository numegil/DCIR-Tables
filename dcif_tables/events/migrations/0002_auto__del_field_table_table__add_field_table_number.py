# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Table.table'
        db.delete_column('events_table', 'table')

        # Adding field 'Table.number'
        db.add_column('events_table', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Table.table'
        raise RuntimeError("Cannot reverse this migration. 'Table.table' and its values cannot be restored.")
        # Deleting field 'Table.number'
        db.delete_column('events_table', 'number')

    models = {
        'events.table': {
            'Meta': {'object_name': 'Table'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['events']