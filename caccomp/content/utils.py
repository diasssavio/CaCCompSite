# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django import template
from django.template.defaultfilters import stringfilter

from models import Post, Document

register = template.Library()

@register.filter
def cut( value, amount ):
	'''Template filter para realizar slice em uma list/string'''
	return value[:amount]