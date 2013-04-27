# -*- encoding: utf-8 -*-

from django import forms

from models import Academic, Post, Keyword, Galery, Document, News, CategoryNews

class FormAcademic( forms.ModelForm ):
	'''
	Formulário ModelForm do acadêmico.
	Cria os campos do formulário de acordo com o model definido
	'''

	class Meta:
		'''
		Permite a personalização do formulário gerado automaticamente
		'''

		model = Academic
		#fields = (  )

class FormPost( forms.ModelForm ):
	'''
	Formulário ModelForm de postagem.
	'''

	class Meta:
		'''
		Permite a personalização do formulário gerado automaticamente
		'''

		model = Post
		#fields = (  )

class FormKeyword( forms.ModelForm ):
	'''
	Formulário ModelForm de palavras-chave.
	'''

	class Meta:
		'''
		Permite a personalização do formulário gerado automaticamente
		'''

		model = Keyword
		#fields = (  )

class FormGalery( forms.ModelForm ):
	'''
	Formulário ModelForm de galeria de imagens.
	'''

	class Meta:
		'''
		Permite a personalização do formulário gerado automaticamente
		'''

		model = Galery
		#fields = (  )

class FormDocument( forms.ModelForm ):
	'''
	Formulário ModelForm de documentos.
	'''

	class Meta:
		'''
		Permite a personalização do formulário gerado automaticamente
		'''

		model = Document
		#fields = (  )

class FormNews( forms.ModelForm ):
	'''
	Formulário ModelForm de notícias.
	'''

	class Meta:
		'''
		Permite a personalização do formulário gerado automaticamente
		'''

		model = News
		#fields = (  )

class FormCategoryNews( forms.ModelForm ):
	'''
	Formulário ModelForm de categoria de notícias.
	'''

	class Meta:
		'''
		Permite a personalização do formulário gerado automaticamente
		'''

		model = CategoryNews
		#fields = (  )