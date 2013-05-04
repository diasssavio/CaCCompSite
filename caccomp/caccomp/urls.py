# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'content.views.index', name = 'home'),

    url(r'^content/', include('content.urls')),
    # Examples:
    # url(r'^$', 'caccomp.views.home', name='home'),
    # url(r'^caccomp/', include('caccomp.foo.urls')),

    # login/logout urls
    # url(r'^login/', 'content.views.login', name = 'login' ),
    url(r'^login/', 'django.contrib.auth.views.login', { 'template_name' : 'login.html' } ),
    # url(r'^logout/', 'content.views.logout_then_login', name = 'logout' ),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', { 'login_url' : '/login/' } ),

    # Admin interface urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# if settings.DEBUG:
# 	urlpatterns += patterns( '', ( r'^media/(?P<path>.*)$', 
# 		'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT } ), )