# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.contrib import admin
from django.contrib.auth.models import User

from content.models import Academic, Post, Keyword, Galery, Document, Category

class AdminAcademic( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	fields = ( 'enrollment', 'role', 'user', 'picture', )
	list_display = ( 'user', 'enrollment', 'role', )

admin.site.register( Academic, AdminAcademic )

class CategoryInline( admin.StackedInline ):
	model = Category

class AdminPost( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	fields = ( 'title', 'content', 'user', 'keywords', )
	list_display = ( 'title', 'content', 'user', )
	inlines = [CategoryInline]

admin.site.register( Post, AdminPost )

class AdminKeyword( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	# personalize how to show data in ScheduleItem admin interface
	fields = ( 'name', )
	list_display = ( 'name', )

# admin.site.register( Keyword, AdminKeyword )

class AdminGalery( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	# personalize how to show data in ScheduleItem admin interface
	fields = ( 'post', )
	list_display = ( 'post', )

admin.site.register( Galery, AdminGalery )

class AdminDocument( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	# personalize how to show data in ScheduleItem admin interface
	fields = ( 'legend', 'path', 'is_image', 'galery', 'post', )
	list_display = ( 'legend', 'path', 'is_image', 'galery', 'post', )

admin.site.register( Document, AdminDocument )

class AdminCategory( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	# personalize how to show data in ScheduleItem admin interface
	fields = ( 'name', 'description', )
	list_display = ( 'name', 'description', )

# admin.site.register( Category, AdminCategory )