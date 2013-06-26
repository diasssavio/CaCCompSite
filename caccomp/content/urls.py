# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Add forms urls
                       url(r'^academic/add/$', 'content.views.addAcademic'),
                       url(r'^post/add/$', 'content.views.addPost'),
                       url(r'^galery/add/$', 'content.views.addGalery'),
                       url(r'^category/add/$', 'content.views.addCategory'),

                       # Show pages urls
                       url(r'^articles/(?P<id>\d+)/$', 'content.views.showArticle'),
                       url(r'^tips/$', 'content.views.listTips'),
                       url(r'^docs/$', 'content.views.listDocs'),

                       # List urls
)