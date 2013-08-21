# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vote'
        db.create_table(u'content_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datevote', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('academic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Academic'])),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Poll'])),
            ('alternative', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Alternative'])),
        ))
        db.send_create_signal(u'content', ['Vote'])

        # Adding model 'Poll'
        db.create_table(u'content_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('datepost', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('datebegin', self.gf('django.db.models.fields.DateTimeField')()),
            ('dateend', self.gf('django.db.models.fields.DateTimeField')()),
            ('academic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Academic'])),
        ))
        db.send_create_signal(u'content', ['Poll'])

        # Adding model 'Events'
        db.create_table(u'content_events', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('datepost', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('dateevent', self.gf('django.db.models.fields.DateField')()),
            ('timebegin', self.gf('django.db.models.fields.TimeField')()),
            ('timeend', self.gf('django.db.models.fields.TimeField')()),
            ('academic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Academic'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['content.Post'], null=True, blank=True)),
        ))
        db.send_create_signal(u'content', ['Events'])

        # Adding model 'Alternative'
        db.create_table(u'content_alternative', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Poll'])),
        ))
        db.send_create_signal(u'content', ['Alternative'])


    def backwards(self, orm):
        # Deleting model 'Vote'
        db.delete_table(u'content_vote')

        # Deleting model 'Poll'
        db.delete_table(u'content_poll')

        # Deleting model 'Events'
        db.delete_table(u'content_events')

        # Deleting model 'Alternative'
        db.delete_table(u'content_alternative')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'content.academic': {
            'Meta': {'object_name': 'Academic'},
            'enrollment': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['content.Document']", 'unique': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'content.alternative': {
            'Meta': {'object_name': 'Alternative'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Poll']"})
        },
        u'content.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'content.document': {
            'Meta': {'object_name': 'Document'},
            'document': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'galery': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['content.Galery']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'legend': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['content.Post']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'content.events': {
            'Meta': {'object_name': 'Events'},
            'academic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Academic']"}),
            'dateevent': ('django.db.models.fields.DateField', [], {}),
            'datepost': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['content.Post']", 'null': 'True', 'blank': 'True'}),
            'timebegin': ('django.db.models.fields.TimeField', [], {}),
            'timeend': ('django.db.models.fields.TimeField', [], {})
        },
        u'content.galery': {
            'Meta': {'object_name': 'Galery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['content.Post']", 'unique': 'True'})
        },
        u'content.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'content.poll': {
            'Meta': {'object_name': 'Poll'},
            'academic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Academic']"}),
            'datebegin': ('django.db.models.fields.DateTimeField', [], {}),
            'dateend': ('django.db.models.fields.DateTimeField', [], {}),
            'datepost': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'content.post': {
            'Meta': {'object_name': 'Post'},
            'academic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Academic']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'datepost': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['content.Keyword']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'view': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'content.vote': {
            'Meta': {'object_name': 'Vote'},
            'academic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Academic']"}),
            'alternative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Alternative']"}),
            'datevote': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Poll']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['content']