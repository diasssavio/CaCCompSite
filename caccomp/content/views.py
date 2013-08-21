# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from models import Academic, Post, Document, Poll, Alternative, Vote, Events
from forms import FormUser, FormAcademic, FormDocument, FormPost, FormGalery, FormCategory, VoteForm

from datetime import datetime, date

# Create your views here.

def index(request):
    # CCOMP_NEWS
    ccompNews = Post.objects.filter(category__name='NEWS_CCOMP').filter(status=True).order_by('-datepost')[:6]

    # UFT_NEWS
    uftNews = Post.objects.filter(category__name='NEWS_UFT').filter(status=True).order_by('-datepost')[:5]

    # LINKS_TIPS
    tips = Post.objects.filter(category__name='LINKS_TIPS').filter(status=True).order_by('-datepost')[:4]

    # DOCS
    docs = Post.objects.filter(category__name='DOCS').filter(status=True).order_by('-datepost')[:4]

    # POLL
    poll = Poll.objects.filter(datebegin__lte=datetime.now()).filter(dateend__gte=datetime.now()).order_by('-datepost')[0]
    voted = False
    if request.method == 'POST':
        voteForm = VoteForm(poll.get_alternatives(), data=request.POST)
        if voteForm.is_valid():
            alternative = Alternative.objects.get(pk=voteForm.cleaned_data['alternative'][0])
            vote = Vote(academic=Academic.objects.get(user=request.user), poll=poll, alternative=alternative)
            vote.save()
            voted = True
    else:
        voteForm = VoteForm(poll.get_alternatives())

    data = {'ccompNews': ccompNews, 'uftNews': uftNews, 'tips': tips, 'docs': docs, 'poll': poll, 'voteForm': voteForm,
            'voted': voted}

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
    most_viewed = Post.objects.filter(category__name='LINKS_TIPS').filter(status=True).order_by('-view')[:4]

    tipsPaginator = Paginator(tip_list, 10)
    page = request.GET.get('page')
    try:
        tips = tipsPaginator.page(page)
    except PageNotAnInteger:
        tips = tipsPaginator.page(1)
    except EmptyPage:
        tips = tipsPaginator.page(tipsPaginator.num_pages)

    return render_to_response('content/tips.html', {'tips': tips, 'most_viewed': most_viewed},
                              context_instance=RequestContext(request))


def listDocs(request):
    doc_list = Post.objects.filter(category__name='DOCS').filter(status=True).order_by('-datepost')
    most_viewed = Post.objects.filter(category__name='DOCS').filter(status=True).order_by('-view')[:4]

    docsPaginator = Paginator(doc_list, 10)
    page = request.GET.get('page')
    try:
        docs = docsPaginator.page(page)
    except PageNotAnInteger:
        docs = docsPaginator.page(1)
    except EmptyPage:
        docs = docsPaginator.page(docsPaginator.num_pages)

    return render_to_response('content/docs.html', {'docs': docs, 'most_viewed': most_viewed},
                              context_instance=RequestContext(request))


def listArticles(request):
    article_list = Post.objects.filter(Q(category__name='NEWS_UFT') | Q(category__name='NEWS_CCOMP')).filter(status=True).order_by('-datepost')
    most_viewed = Post.objects.filter(Q(category__name='NEWS_UFT') | Q(category__name='NEWS_CCOMP')).filter(status=True).order_by('-view')[:4]

    articlesPaginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    try:
        articles = articlesPaginator.page(page)
    except PageNotAnInteger:
        articles = articlesPaginator.page(1)
    except EmptyPage:
        articles = articlesPaginator.page(articlesPaginator.num_pages)

    return render_to_response('content/articles.html', {'articles': articles, 'most_viewed': most_viewed},
                              context_instance=RequestContext(request))


def showArticle(request, id):
    article = get_object_or_404(Post, Q(pk=id), Q(category__name='NEWS_CCOMP') | Q(category__name='NEWS_UFT'))
    article.view += 1
    article.save()

    return render_to_response('content/article.html', {'article': article}, context_instance=RequestContext(request))


def documentPageCount(request, id):
    post = get_object_or_404(Post, pk=id)
    post.view += 1
    post.save()

    return HttpResponseRedirect('/media/' + post.get_document().document.__str__())


def tipsPageCount(request, id):
    post = get_object_or_404(Post, pk=id)
    post.view += 1
    post.save()

    return HttpResponseRedirect(post.get_link().url.__str__())


def listPolls(request):
    #lista de enquetes abertos para votação
    poll_list = Poll.objects.filter(datebegin__lte=datetime.now()).filter(dateend__gte=datetime.now()).order_by('-datepost')

    #lista de enquetes que vão abrir
    poll_list_future = Poll.objects.filter(datebegin__gt=datetime.now()).order_by('-datepost')

    #lista de enquetes que já fecharam
    poll_list_pass =  Poll.objects.filter(dateend__lt=datetime.now()).order_by('-datepost')

    pollsPaginator = Paginator(poll_list, 5)
    page = request.GET.get('page')
    try:
        polls = pollsPaginator.page(page)
    except PageNotAnInteger:
        polls = pollsPaginator.page(1)
    except EmptyPage:
        polls = pollsPaginator.page(pollsPaginator.num_pages)

    pollsFuturePaginator = Paginator(poll_list_future, 5)
    page = request.GET.get('pageFuture')
    try:
        pollsFuture = pollsFuturePaginator.page(page)
    except PageNotAnInteger:
        pollsFuture = pollsFuturePaginator.page(1)
    except EmptyPage:
        pollsFuture = pollsFuturePaginator.page(pollsFuturePaginator.num_pages)

    pollsPassPaginator = Paginator(poll_list_pass, 5)
    page = request.GET.get('pagePass')
    try:
        pollsPass = pollsPassPaginator.page(page)
    except PageNotAnInteger:
        pollsPass = pollsPassPaginator.page(1)
    except EmptyPage:
        pollsPass = pollsPassPaginator.page(pollsPassPaginator.num_pages)

    return render_to_response('content/polls.html', {'polls': polls, 'pollsFuture': pollsFuture, 'pollsPass': pollsPass, }, context_instance=RequestContext(request))

def votingPoll(request, id):
    voting = get_object_or_404(Vote, Q(pk=id))
    #voting.view += 1
    #voting.save()

    return render_to_response('content/polls.html', {'voting': voting}, context_instance=RequestContext(request))
    pass

def listEvents(request):
    #lista de eventos de hoje
    events_list_today = Events.objects.filter(dateevent__gte=date.today()).order_by('-dateevent').order_by('timebegin')

    #lista de eventos de amanhã
    #events_list_tomorrow = Events.objects.filter(datebegin__gt=datetime.now()).order_by('-datebegin')
    # data = {'today': events_list_today, 'tomorrow': events_list_tomorrow}
    # return render_to_response('content/events.html', data, context_instance=RequestContext(request))

    return render_to_response('content/events.html', {'events_list_today': events_list_today}, context_instance=RequestContext(request))
