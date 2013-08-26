# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'baygon.views.listDoubts'),
)