# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.db import models
from content.models import Academic, Keyword

# Create your models here.

class Doubt(models.Model):
    asking = models.CharField(max_length=255, verbose_name=u'Pergunta/Dúvida')
    datepost = models.DateTimeField(auto_now_add=True)
    explanation = models.TextField(null=True, default=None, blank=True, verbose_name=u'Explicação')
    code = models.TextField(null=True, default=None, blank=True, verbose_name=u'Código')
    popularity = models.PositiveIntegerField(default=0, verbose_name=u'Popularidade')
    view = models.PositiveIntegerField(default=0, verbose_name=u'Visualizações')

    keywords = models.ManyToManyField(Keyword, verbose_name='Palavras-Chave')
    academic = models.ForeignKey(Academic, verbose_name=u'Acadêmico')

    def get_answers(self):
        return Answer.objects.filter(doubt=self)

    def __unicode__(self):
        return '%s' % self.asking

    class Meta:
        verbose_name = 'Pergunta/Dúvida'
        verbose_name_plural = 'Perguntas/Dúvidas'


class Answer(models.Model):
    explanation = models.TextField(verbose_name=u'Explicação')
    datepost = models.DateTimeField(auto_now_add=True)
    code = models.TextField(null=True, default=None, blank=True, verbose_name=u'Código')
    popularity = models.PositiveIntegerField(default=0, verbose_name=u'Popularidade')

    academic = models.ForeignKey(Academic, verbose_name=u'Acadêmico')
    doubt = models.ForeignKey(Doubt, verbose_name=u'Dúvida')

    def __unicode__(self):
        return '%s' % self.explanation[:45]

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'