# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import Academic, Post, Keyword, Galery, Document, Category


class VoteForm(forms.Form):
    def __init__(self, alternatives, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['alternative'] = forms.ChoiceField(choices=[(alternative.pk, alternative.name) for alternative in alternatives], widget=forms.RadioSelect())


class FormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email',  )


class FormAcademic(forms.ModelForm):
    '''
	Formulário ModelForm do acadêmico.
	Cria os campos do formulário de acordo com o model definido
	'''

    class Meta:
        '''
		Permite a personalização do formulário gerado automaticamente
		'''

        model = Academic
        fields = ( 'enrollment', 'role', 'picture', )


class FormPost(forms.ModelForm):
    '''
	Formulário ModelForm de postagem.
	'''

    class Meta:
        '''
		Permite a personalização do formulário gerado automaticamente
		'''

        model = Post
        fields = ( 'title', 'content', 'category', 'keywords', )


class FormKeyword(forms.ModelForm):
    '''
	Formulário ModelForm de palavras-chave.
	'''

    class Meta:
        '''
		Permite a personalização do formulário gerado automaticamente
		'''

        model = Keyword
        fields = ( 'name', )


class FormGalery(forms.ModelForm):
    '''
	Formulário ModelForm de galeria de imagens.
	'''

    class Meta:
        '''
		Permite a personalização do formulário gerado automaticamente
		'''

        model = Galery
        fields = ( 'post', )


class FormDocument(forms.ModelForm):
    '''
	Formulário ModelForm de documentos.
	'''

    class Meta:
        '''
		Permite a personalização do formulário gerado automaticamente
		'''

        model = Document
        fields = ( 'legend', 'document', 'image', 'galery', 'post', )


class FormCategory(forms.ModelForm):
    '''
	Formulário ModelForm de categoria de notícias.
	'''

    class Meta:
        '''
		Permite a personalização do formulário gerado automaticamente
		'''

        model = Category
        fields = ( 'name', 'description', )