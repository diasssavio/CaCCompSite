# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Popularity'
        db.create_table(u'baygon_popularity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('academic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Academic'])),
            ('doubt', self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['baygon.Doubt'], unique=True, null=True, blank=True)),
            ('answer', self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['baygon.Answer'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'baygon', ['Popularity'])

        # Adding model 'Language'
        db.create_table(u'baygon_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('brush', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'baygon', ['Language'])

        # Deleting field 'Doubt.popularity'
        db.delete_column(u'baygon_doubt', 'popularity')

        # Adding field 'Doubt.language'
        db.add_column(u'baygon_doubt', 'language',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['baygon.Language'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Answer.popularity'
        db.delete_column(u'baygon_answer', 'popularity')

        # Adding field 'Answer.language'
        db.add_column(u'baygon_answer', 'language',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['baygon.Language'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Popularity'
        db.delete_table(u'baygon_popularity')

        # Deleting model 'Language'
        db.delete_table(u'baygon_language')

        # Adding field 'Doubt.popularity'
        db.add_column(u'baygon_doubt', 'popularity',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Doubt.language'
        db.delete_column(u'baygon_doubt', 'language_id')

        # Adding field 'Answer.popularity'
        db.add_column(u'baygon_answer', 'popularity',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Answer.language'
        db.delete_column(u'baygon_answer', 'language_id')


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
        u'baygon.answer': {
            'Meta': {'object_name': 'Answer'},
            'academic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Academic']"}),
            'code': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'datepost': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'doubt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['baygon.Doubt']"}),
            'explanation': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['baygon.Language']", 'null': 'True', 'blank': 'True'})
        },
        u'baygon.doubt': {
            'Meta': {'object_name': 'Doubt'},
            'academic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Academic']"}),
            'asking': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'code': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'datepost': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'explanation': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['content.Keyword']", 'symmetrical': 'False'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['baygon.Language']", 'null': 'True', 'blank': 'True'}),
            'view': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'baygon.language': {
            'Meta': {'object_name': 'Language'},
            'brush': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'baygon.popularity': {
            'Meta': {'object_name': 'Popularity'},
            'academic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Academic']"}),
            'answer': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'to': u"orm['baygon.Answer']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'doubt': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'to': u"orm['baygon.Doubt']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'content.academic': {
            'Meta': {'object_name': 'Academic'},
            'enrollment': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['content.Document']", 'unique': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['baygon']