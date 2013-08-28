# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.db import models
from content.models import Academic, Keyword

# Create your models here.

class Doubt(models.Model):
    asking = models.CharField(max_length=255, verbose_name=u'Pergunta/Dúvida')
    datepost = models.DateTimeField(auto_now_add=True)
    explanation = models.TextField(verbose_name=u'Explicação')
    code = models.TextField(null=True, default=None, blank=True, verbose_name=u'Código-Fonte')
    view = models.PositiveIntegerField(default=0, verbose_name=u'Visualizações')

    language = models.ForeignKey('Language', null=True, default=None, blank=True, verbose_name='Linguagem')
    keywords = models.ManyToManyField(Keyword, verbose_name='Palavras-Chave')
    academic = models.ForeignKey(Academic, verbose_name=u'Acadêmico')

    def get_answers(self):
        return Answer.objects.filter(doubt=self)

    def get_popularity(self):
        return Popularity.objects.filter(doubt=self)

    def __unicode__(self):
        return '%s' % self.asking

    class Meta:
        verbose_name = 'Pergunta/Dúvida'
        verbose_name_plural = 'Perguntas/Dúvidas'


class Answer(models.Model):
    explanation = models.TextField(verbose_name=u'Explicação')
    datepost = models.DateTimeField(auto_now_add=True)
    code = models.TextField(null=True, default=None, blank=True, verbose_name=u'Código-Fonte')

    language = models.ForeignKey('Language', null=True, default=None, blank=True, verbose_name='Linguagem')
    academic = models.ForeignKey(Academic, verbose_name=u'Acadêmico')
    doubt = models.ForeignKey(Doubt, verbose_name=u'Dúvida')

    def __unicode__(self):
        return '%s' % self.explanation[:45]

    def get_popularity(self):
        return Popularity.objects.filter(answer=self)

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'


class Language(models.Model):
    name = models.CharField(max_length=45, verbose_name='Linguagem')
    brush = models.CharField(max_length=45, verbose_name='Brush do highlighter')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Linguagem'
        verbose_name_plural = 'Linguagens'


class Popularity(models.Model):
    academic = models.ForeignKey(Academic, verbose_name=u'Acadêmico')
    doubt = models.OneToOneField(Doubt, null=True, default=None, blank=True, verbose_name=u'Dúvida votada')
    answer = models.OneToOneField(Answer, null=True, default=None, blank=True, verbose_name=u'Resposta votada')

    class Meta:
        verbose_name = 'Popularidade'
        verbose_name_plural = 'Popularidades'