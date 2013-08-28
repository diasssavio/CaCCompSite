# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.contrib import admin
from content.models import Academic
from baygon.models import Answer, Doubt, Language


class AnswerInline(admin.StackedInline):
    model = Answer
    fields = ('explanation', 'code', 'language')
    can_delete = True
    extra = 1


class AdminDoubt(admin.ModelAdmin):
    fields = ('asking', 'explanation', 'code', 'language', 'keywords',)
    list_display = ('asking', 'academic', 'datepost', 'popularity', 'view',)
    inlines = [AnswerInline]

    def save_model(self, request, obj, form, change):
        obj.academic = Academic.objects.get(user=request.user)
        obj.save()

    def save_formset(self, request, form, formset, change):
        for instance in formset.save(commit=False):
            instance.academic = Academic.objects.get(user=request.user)
            instance.save()
        formset.save_m2m()

admin.site.register(Doubt, AdminDoubt)


class AdminLanguage(admin.ModelAdmin):
    fields = ('name', 'brush',)
    list_display = ('name', 'brush',)

admin.site.register(Language, AdminLanguage)