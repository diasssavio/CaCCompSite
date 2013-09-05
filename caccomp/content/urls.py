# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^academic/add/$', 'content.views.addAcademic'),
                       url(r'^post/add/$', 'content.views.addPost'),
                       url(r'^galery/add/$', 'content.views.addGalery'),
                       url(r'^category/add/$', 'content.views.addCategory'),

                       # Show pages urls
                       url(r'^articles/(?P<id>\d+)/$', 'content.views.showArticle'),
                       url(r'^articles/$', 'content.views.listArticles'),
                       url(r'^tips/$', 'content.views.listTips'),
                       url(r'^docs/$', 'content.views.listDocs'),
                       url(r'^polls/$', 'content.views.listPolls'),
                       url(r'^events/$', 'content.views.listEvents'),
                       url(r'^galery/$', 'content.views.listGalery'),

                       # Voting Poll
                       url(r'^polls/(?P<id>\d+)/$', 'content.views.votingPoll'),

                       # List urls

                       # Count urls
                       url(r'^doccount/(?P<id>\d+)', 'content.views.documentPageCount'),
                       url(r'^tipscount/(?P<id>\d+)', 'content.views.tipsPageCount'),
)