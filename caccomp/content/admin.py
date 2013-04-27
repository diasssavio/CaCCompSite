# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.contrib import admin

from content.models import Academic, Post, Keyword, Galery, Document, News, CategoryNews

class AdminKeyword( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	# personalize how to show data in ScheduleItem admin interface
	fields = ( 'name', )
	list_display = ( 'name', )

admin.site.register( Keyword, AdminKeyword )

class AdminCategoryNews( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	# personalize how to show data in ScheduleItem admin interface
	fields = ( 'name', 'description', )
	list_display = ( 'name', 'description', )

admin.site.register( CategoryNews, AdminCategoryNews )