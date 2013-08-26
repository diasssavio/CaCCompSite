# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.contrib import admin
from content.models import Academic
from baygon.models import Answer, Doubt


class AnswerInline(admin.StackedInline):
    model = Answer
    fields = ('explanation', 'code',)
    can_delete = True
    extra = 1


class AdminDoubt(admin.ModelAdmin):
    fields = ('asking', 'explanation', 'code', 'keywords',)
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