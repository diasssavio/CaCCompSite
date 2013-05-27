# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Academic( models.Model ):
	'''
	Model que representa a tabela de acadêmicos
	'''

	enrollment = models.IntegerField( verbose_name = u'matrícula' )
	role = models.CharField( max_length = 45, verbose_name = u'função' )

	picture = models.OneToOneField( 'Document', verbose_name = u'Imagem' )

	user = models.OneToOneField( User, verbose_name = u'Usuário' )

	def __unicode__( self ):
		return '%s %s' % ( self.user.first_name, self.user.last_name )

	class Meta:
		verbose_name = u'Acadêmico'

class Post( models.Model ):
	'''
	Model que representa a tabela de postagens
	'''

	title = models.CharField( max_length = 255 )
	datepost = models.DateTimeField( auto_now_add = True )
	content = models.TextField( null = True, default = None, blank = True )
	status = models.BooleanField( default = False )

	academic = models.ForeignKey( Academic )
	category = models.ForeignKey( 'Category' )
	keywords = models.ManyToManyField( 'Keyword' )

	def __unicode__( self ):
		return '%s - %s' % ( self.title, self.datepost.strftime( '%H:%Mhrs %d/%m/%Y' ) )

	class Meta:
		verbose_name = 'Postagem'

class Keyword( models.Model ):
	'''
	Model que representa a tabela de palavras-chave
	'''

	name = models.CharField( max_length = 45 )

	def __unicode__( self ):
		return '%s' % ( self.name )

	class Meta:
		verbose_name = 'Palavra-chave'

class Galery( models.Model ):
	'''
	Model que representa a tabela de galerias
	'''

	post = models.OneToOneField( Post )

	class Meta:
		verbose_name = 'Galeria'

class Document( models.Model ):
	'''
	Model que representa a tabela de documentos
	'''

	legend = models.CharField( max_length = 45 )
	document = models.FileField( upload_to = 'content/documents', null = True, default = None, blank = True )
	image = models.FileField( upload_to = 'content/pictures', null = True, default = None, blank = True, verbose_name = 'Imagem' )
	url = models.CharField( max_length = 255, null = True, default = None, blank = True )

	galery = models.ForeignKey( Galery, null = True, default = None, blank = True )
	post = models.ForeignKey( Post, null = True, default = None, blank = True )

	def __unicode__( self ):
		return '%s' % ( self.legend )

	class Meta:
		verbose_name = 'Documento'

class Category( models.Model ):
	'''
	Model que representa a tabela de categoria de notícias
	'''

	name = models.CharField( max_length = 45 )
	description = models.CharField( max_length = 255 )

	def __unicode__( self ):
		return '%s' % ( self.name )

	class Meta:
		verbose_name = u'Categoria-Notícia'