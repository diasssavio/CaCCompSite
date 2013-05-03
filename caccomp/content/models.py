# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Academic( models.Model ):
	'''
	Model que representa a tabela de acadêmicos
	'''

	enrollment = models.IntegerField()
	role = models.CharField( max_length = 45 )

	user = models.OneToOneField( User )
	picture = models.OneToOneField( 'Document' )

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

	user = models.ForeignKey( User )
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
	path = models.FileField( upload_to = 'content/pictures' )
	is_image = models.BooleanField()

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