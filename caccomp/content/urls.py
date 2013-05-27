# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	# Add forms urls
	url(r'^academic/add/$', 'content.views.addAcademic'),
	url(r'^post/add/$', 'content.views.addPost'),
	url(r'^galery/add/$', 'content.views.addGalery'),
	url(r'^category/add/$', 'content.views.addCategory'),
	url(r'^tips/$', 'content.views.listTips'),

	# List urls
)