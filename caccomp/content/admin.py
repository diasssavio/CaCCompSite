# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from content.models import Academic, Post, Keyword, Galery, Document, Category, Vote, Poll, Alternative, Events


class academicInline(admin.StackedInline):
    model = Academic
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = [academicInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class AdminAcademic(admin.ModelAdmin):
    '''
	Classe para personalizar a interface de admin
	'''

    fields = ( 'enrollment', 'role', 'user', 'picture', )
    list_display = ( 'user', 'enrollment', 'role', )

# admin.site.register( Academic, AdminAcademic )

class AdminPost(admin.ModelAdmin):
    '''
	Classe para personalizar a interface de admin
	'''

    fields = ('title', 'content', 'academic', 'category', 'keywords', 'status',)
    list_display = ('pk', 'title', 'content', 'academic', 'category', 'status',)


admin.site.register(Post, AdminPost)


class AdminKeyword(admin.ModelAdmin):
    '''
	Classe para personalizar a interface de admin
	'''

    fields = ( 'name', )
    list_display = ( 'name', )


admin.site.register(Keyword, AdminKeyword)


class AdminGalery(admin.ModelAdmin):
    '''
	Classe para personalizar a interface de admin
	'''

    fields = ( 'post', )
    list_display = ( 'post', )


admin.site.register(Galery, AdminGalery)


class AdminDocument(admin.ModelAdmin):
    '''
	Classe para personalizar a interface de admin
	'''

    fields = ( 'legend', 'document', 'image', 'url', 'galery', 'post', )
    list_display = ( 'legend', 'document', 'image', 'url', 'galery', 'post', )


admin.site.register(Document, AdminDocument)


class AdminCategory(admin.ModelAdmin):
    '''
	Classe para personalizar a interface de admin
	'''

    fields = ( 'name', 'description', )
    list_display = ( 'name', )


admin.site.register(Category, AdminCategory)


class alternativeInline(admin.StackedInline):
    model = Alternative
    can_delete = False


class AdminPoll(admin.ModelAdmin):
    '''
    Classe para personalizar a interface de admin
    '''

    fields = ( 'title', 'datebegin', 'dateend', 'academic', )
    list_display = ( 'pk', 'title', 'datebegin', 'dateend', 'academic', )

    inlines = [alternativeInline]


admin.site.register(Poll, AdminPoll)


class AdminVote(admin.ModelAdmin):
    '''
    Classe para personalizar a interface de admin
    '''

    fields = ( 'academic', 'poll', 'alternative', )
    list_display = ( 'pk', 'academic', 'poll', 'alternative', )


admin.site.register(Vote, AdminVote)


class AdminEvents(admin.ModelAdmin):
    '''
    Classe para personalizar a interface de admin
    '''

    fields = ( 'name', 'dateevent', 'timebegin', 'timeend', 'academic', 'post', )
    list_display = ( 'pk', 'name', 'dateevent', 'timebegin', 'timeend', 'academic', 'post', )


admin.site.register(Events, AdminEvents)
