# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist

from models import Academic, Post, Document
from forms import FormUser, FormAcademic, FormDocument, FormPost, FormGalery, FormCategory

# Create your views here.

def index(request, user=None):
    # CCOMP_NEWS
    ccompNews = Post.objects.filter(category__name='NEWS_CCOMP').filter(status=True).order_by('-datepost')[:6]

    # UFT_NEWS
    uftNews = Post.objects.filter(category__name='NEWS_UFT').filter(status=True).order_by('-datepost')[:5]

    # LINKS_TIPS
    tips = Post.objects.filter(category__name='LINKS_TIPS').filter(status=True).order_by('-datepost')[:4]

    # DOCS
    docs = Post.objects.filter(category__name='DOCS').filter(status=True).order_by('-datepost')[:4]

    data = {'ccompNews': ccompNews, 'uftNews': uftNews, 'tips': tips, 'docs': docs}

    return render_to_response('content/home.html', data, context_instance=RequestContext(request))


def addAcademic(request):
    if request.method == 'POST':
        formAcademic = FormAcademic(data=request.POST)
        formUser = FormUser(data=request.POST)
        formDocument = FormDocument(data=request.POST)
        if formUser.is_valid() and formDocument.is_valid():
            # User
            user = formUser.save()

            # Document
            document = formDocument.save(commit=False)
            document.legend = document.image.__str__()
            document.save()

            # Academic
            academic = formAcademic.save(commit=False)
            academic.user = user
            academic.picture = document
            academic.save()
            return render_to_response('content/saved.html', {'name': u'Acadêmico', 'this': 'academic/add/'})
    else:
        formAcademic = FormAcademic()
        formUser = FormUser()
        formDocument = FormDocument()

    return render_to_response('content/addAcademic.html', {'formAcademic': formAcademic, 'formUser': formUser,
                                                           'formDocument': formDocument},
                              context_instance=RequestContext(request))


@login_required
def addPost(request):
    if request.method == 'POST':
        form = FormPost(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            item.academic = Academic.objects.get(user__pk=request.user.pk)
            item.save()
            return render_to_response('content/saved.html', {'name': u'Postagem', 'this': 'post/add/'})
    else:
        form = FormPost()

    return render_to_response('addPost.html', {'form', form}, context_instance=RequestContext(request))


@login_required
def addGalery(request):
    if request.method == 'POST':
        form = FormGalery(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('saved.html', {'name': u'Galeria', 'this': 'galery/add/'})
    else:
        form = FormGalery()

    return render_to_response('addGalery.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def addCategory(request):
    if request.method == 'POST' and request.user.is_superuser:
        form = FormCategory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('saved.html', {'name': u'Categoria', 'this': 'category/add/'})
    else:
        form = FormGalery()

    return render_to_response('addCategory.html', {'form': form}, context_instance=RequestContext(request))


def listTips(request):
    tip_list = Post.objects.filter(category__name='LINKS_TIPS').filter(status=True).order_by('-datepost')

    tipsPaginator = Paginator(tip_list, 10)
    page = request.GET.get('page')
    try:
        tips = tipsPaginator.page(page)
    except PageNotAnInteger:
        tips = tipsPaginator.page(1)
    except EmptyPage:
        tips = tipsPaginator.page(tipsPaginator.num_pages)

    return render_to_response('content/tips.html', {'tips': tips}, context_instance=RequestContext(request))


def listDocs(request):
    doc_list = Post.objects.filter(category__name='DOCS').filter(status=True).order_by('-datepost')

    docsPaginator = Paginator(doc_list, 10)
    page = request.GET.get('page')
    try:
        docs = docsPaginator.page(page)
    except PageNotAnInteger:
        docs = docsPaginator.page(1)
    except EmptyPage:
        docs = docsPaginator.page(docsPaginator.num_pages)

    return render_to_response('content/docs.html', {'docs': docs}, context_instance=RequestContext(request))


def showArticle(request, id):
    article = get_object_or_404(Post, Q(pk=id), Q(category__name='NEWS_CCOMP') | Q(category__name='NEWS_UFT'))

    return render_to_response('content/showArticle.html', {'article': article}, context_instance=RequestContext(request))