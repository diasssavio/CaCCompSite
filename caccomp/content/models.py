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

	enrollment = models.IntegerField( verbose_name = u'Matrícula' )
	role = models.CharField( max_length = 45, verbose_name = u'Função' )

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

	title = models.CharField( max_length = 255, verbose_name = u'Título' )
	datepost = models.DateTimeField( auto_now_add = True )
	content = models.TextField( null = True, default = None, blank = True, verbose_name = u'Conteúdo' )
	status = models.BooleanField( default = False )

	academic = models.ForeignKey( Academic, verbose_name = 'Acadêmico' )
	category = models.ForeignKey( 'Category', verbose_name = 'Categoria' )
	keywords = models.ManyToManyField( 'Keyword', verbose_name = 'Palavras-Chave' )

	def get_picture( self ):
		return Document.objects.filter( post = self ).filter( image__isnull = False )[0]

	def get_pictures( self ):
		return Document.objects.filter( post = self ).filter( image__isnull = False )

	def get_link( self ):
		return Document.objects.filter( post = self ).filter( url__isnull = False )[0]

	def get_document( self ):
		return Document.objects.filter( post = self ).filter( document__isnull = False )[0]

	def __unicode__( self ):
		return '%s - %s' % ( self.title, self.datepost.strftime( '%H:%Mhrs %d/%m/%Y' ) )

	class Meta:
		verbose_name = 'Postagem'

class Keyword( models.Model ):
	'''
	Model que representa a tabela de palavras-chave
	'''

	name = models.CharField( max_length = 45, verbose_name = 'Nome' )

	def __unicode__( self ):
		return '%s' % ( self.name )

	class Meta:
		verbose_name = 'Palavra-chave'

class Galery( models.Model ):
	'''
	Model que representa a tabela de galerias
	'''

	post = models.OneToOneField( Post, verbose_name = 'Postagem' )

	class Meta:
		verbose_name = 'Galeria'

class Document( models.Model ):
	'''
	Model que representa a tabela de documentos
	'''

	legend = models.CharField( max_length = 45, verbose_name = 'Legenda' )
	document = models.FileField( upload_to = 'content/documents', null = True, default = None, blank = True, verbose_name = 'Documento' )
	image = models.FileField( upload_to = 'content/pictures', null = True, default = None, blank = True, verbose_name = 'Imagem' )
	url = models.CharField( max_length = 255, null = True, default = None, blank = True )

	galery = models.ForeignKey( Galery, null = True, default = None, blank = True, verbose_name = 'Galeria' )
	post = models.ForeignKey( Post, null = True, default = None, blank = True, verbose_name = 'Post' )

	def __unicode__( self ):
		return '%s' % ( self.legend )

	class Meta:
		verbose_name = 'Documento'

class Category( models.Model ):
	'''
	Model que representa a tabela de categoria de notícias
	'''

	name = models.CharField( max_length = 45, verbose_name = 'Nome' )
	description = models.CharField( max_length = 255, verbose_name = u'Descrição' )

	def __unicode__( self ):
		return '%s' % ( self.name )

	class Meta:
		verbose_name = u'Categoria-Notícia'