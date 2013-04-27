# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Keyword
from forms import FormKeyword

# Create your views here.

def addKey( request ):
	'''
	Adiciona um novo elemento. Faz a validação e salva como\
	pertencendo ao usuário em sessão
	'''

	if request.method == 'POST' :
		form = FormKeyword( request.POST, request.FILES )
		if form.is_valid():
			form.save()
			
			return render_to_response( 'salvo.html', {} )
	else:
		form = FormKeyword()

	return render_to_response( 'addkey.html', { 'form' : form }, 
			context_instance = RequestContext( request ) )