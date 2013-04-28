# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.contrib import admin

from content.models import Academic, Post, Keyword, Galery, Document, News, CategoryNews

class AdminAcademic( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	fields = ( 'enrollment', 'role', 'user', 'picture', )
	list_display = ( 'user', 'enrollment', 'role', )

admin.site.register( Academic, AdminAcademic )

class AdminPost( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	fields = ( 'title', 'content', 'user', 'keywords' )
	list_display = ( 'title', 'content', 'user' )

admin.site.register( Post, AdminPost )

class AdminKeyword( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	# personalize how to show data in ScheduleItem admin interface
	fields = ( 'name', )
	list_display = ( 'name', )

admin.site.register( Keyword, AdminKeyword )

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
	fields = ( 'legend', 'path', 'is_img', 'galery', 'post', )
	list_display = ( 'legend', 'path', 'is_img', 'galery', 'post', )

admin.site.register( Document, AdminDocument )

class AdminNews( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	# personalize how to show data in ScheduleItem admin interface
	fields = ( 'content', 'categorynews', 'post', )
	list_display = ( 'content', 'categorynews', 'post', )

admin.site.register( News, AdminNews )

class AdminCategoryNews( admin.ModelAdmin ):
	'''
	Classe para personalizar a interface de admin
	'''

	# personalize how to show data in ScheduleItem admin interface
	fields = ( 'name', 'description', )
	list_display = ( 'name', 'description', )

admin.site.register( CategoryNews, AdminCategoryNews )