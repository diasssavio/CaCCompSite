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

class Post( models.Model ):
	'''
	Model que representa a tabela de postagens
	'''

	title = models.CharField( max_length = 255 )
	datePost = models.DateTimeField( auto_now_add = True )
	content = models.TextField()

	user = models.ForeignKey( User )
	keywords = models.ManyToManyField( 'Keyword' )

class Keyword( models.Model ):
	'''
	Model que representa a tabela de palavras-chave
	'''

	name = models.CharField( max_length = 45 )

class Galery( models.Model ):
	'''
	Model que representa a tabela de galerias
	'''

	post = models.OneToOneField( Post )

class Document( models.Model ):
	'''
	Model que representa a tabela de documentos
	'''

	legend = models.CharField( max_length = 45 )
	path = models.CharField( max_length = 255 )
	is_img = models.BooleanField()
	galery = models.ForeignKey( Galery, null = True, default = None )
	post = models.ForeignKey( Post, null = True, default = None )

class News( models.Model ):
	'''
	Model que representa a tabela de notícias
	'''

	content = models.CharField( max_length = 45 )
	categoryNews = models.ForeignKey( 'CategoryNews' )
	post = models.OneToOneField( Post )

class CategoryNews( models.Model ):
	'''
	Model que representa a tabela de categoria de notícias
	'''

	name = models.CharField( max_length = 45 )
	description = models.CharField( max_length = 255 )