# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Academic'
        db.create_table(u'content_academic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enrollment', self.gf('django.db.models.fields.IntegerField')()),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('picture', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Document'], unique=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'content', ['Academic'])

        # Adding model 'Post'
        db.create_table(u'content_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('datepost', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('academic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Academic'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Category'])),
        ))
        db.send_create_signal(u'content', ['Post'])

        # Adding M2M table for field keywords on 'Post'
        m2m_table_name = db.shorten_name(u'content_post_keywords')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'content.post'], null=False)),
            ('keyword', models.ForeignKey(orm[u'content.keyword'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'keyword_id'])

        # Adding model 'Keyword'
        db.create_table(u'content_keyword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'content', ['Keyword'])

        # Adding model 'Galery'
        db.create_table(u'content_galery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Post'], unique=True)),
        ))
        db.send_create_signal(u'content', ['Galery'])

        # Adding model 'Document'
        db.create_table(u'content_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('legend', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('document', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('galery', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['content.Galery'], null=True, blank=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['content.Post'], null=True, blank=True)),
        ))
        db.send_create_signal(u'content', ['Document'])

        # Adding model 'Category'
        db.create_table(u'content_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'content', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Academic'
        db.delete_table(u'content_academic')

        # Deleting model 'Post'
        db.delete_table(u'content_post')

        # Removing M2M table for field keywords on 'Post'
        db.delete_table(db.shorten_name(u'content_post_keywords'))

        # Deleting model 'Keyword'
        db.delete_table(u'content_keyword')

        # Deleting model 'Galery'
        db.delete_table(u'content_galery')

        # Deleting model 'Document'
        db.delete_table(u'content_document')

        # Deleting model 'Category'
        db.delete_table(u'content_category')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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