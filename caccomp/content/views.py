# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from models import Academic
from forms import FormUser, FormAcademic, FormPost, FormGalery, FormCategory

# Create your views here.

def login( request ):
	'''
	Função para autenticar e logar usuário
	'''
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate( username = username, password = password )
		if user is not None:
			if user.is_active:
				login( request, user )
				# Redirect to a success page.
			else:
				# Return a 'disabled account' error message
				pass
		else:
			# Return an 'invalid login' error message.
			pass
	else:
		pass

def logout_then_login( request ):
	'''
	Função para deslogar usuário e redirecionar ele para tela de login
	'''
	logout( request )
	# Redirect to a success page.

def index( request, user = None ):
	pass

def addAcademic( request ):
	if request.method == 'POST':
		formAcademic = FormAcademic( data = request.POST )
		formUser = FormUser( data = request.POST )
		if formAcademic.is_valid() and formUser.is_valid():
			# User
			user = formUser.save( commit = False )

			# Academic
			academic = formAcademic.save( commit = False )
			academic.user = user
			academic.save()
			return render_to_response( 'saved.html', { 'name' : u'Acadêmico', 'this' : 'academic/add/' } )
	else:
		formAcademic = FormAcademic()
		formUser = FormUser()

	return render_to_response( 'content/addAcademic.html', { 'formAcademic' : formAcademic, 'formUser' : formUser },
								context_instance = RequestContext( request ) )

@login_required
def addPost( request ):
	if request.method == 'POST':
		form = FormPost( request.POST, request.FILES )
		if form.is_valid():
			item = form.save()
			item.academic = Academic.objects.get( user__pk = request.user.pk )
			item.save()
			return render_to_response( 'saved.html', { 'name' : u'Postagem', 'this' : 'post/add/' } )
	else:
		form = FormPost()

	return render_to_response( 'addPost.html', { 'form', form }, context_instance = RequestContext( request ) )

@login_required
def addGalery( request ):
	if request.method == 'POST':
		form = FormGalery( request.POST, request.FILES )
		if form.is_valid():
			form.save()
			return render_to_response( 'saved.html', { 'name' : u'Galeria', 'this' : 'galery/add/' } )
	else:
		form = FormGalery()

	return render_to_response( 'addGalery.html', { 'form' : form }, context_instance = RequestContext( request ) )

@login_required
def addCategory( request ):
	if request.method == 'POST' and request.user.is_superuser:
		form = FormCategory( request.POST, request.FILES )
		if form.is_valid():
			form.save()
			return render_to_response( 'saved.html', { 'name' : u'Categoria', 'this' : 'category/add/' } )
	else:
		form = FormGalery()

	return render_to_response( 'addCategory.html', { 'form' : form }, context_instance = RequestContext( request ) )