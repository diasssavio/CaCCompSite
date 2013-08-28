# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import Answer


class FormAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('explanation', 'code', 'language',)

    def __init__(self, *args, **kwargs):
        super(FormAnswer, self).__init__(*args, **kwargs)
        self.fields['explanation'].widget.attrs.update({'style': 'width: 100%', 'rows': '6'})
        self.fields['code'].widget.attrs.update({'style': 'width: 100%', 'rows': '6'})