# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from content.models import Academic
from baygon.models import Doubt, Answer
from baygon.forms import FormAnswer

# Create your views here.

def listDoubts(request):
    doubt_list = Doubt.objects.all().order_by('-datepost')
    most_viewed = Doubt.objects.all().order_by('-view')[:10]
    most_popular = Doubt.objects.all().order_by('-popularity')[:10]

    doubtsPaginator = Paginator(doubt_list, 10)
    page = request.GET.get('page')
    try:
        doubts = doubtsPaginator.page(page)
    except PageNotAnInteger:
        doubts = doubtsPaginator.page(1)
    except EmptyPage:
        doubts = doubtsPaginator.page(doubtsPaginator.num_pages)

    return render_to_response('baygon/doubts.html', {'doubts': doubts, 'most_viewed': most_viewed,
                              'most_popular': most_popular}, context_instance=RequestContext(request))

def showDoubt(request, id):
    doubt = get_object_or_404(Doubt, pk=id)
    doubt.view += 1
    doubt.save()

    commented = False
    if request.method == 'POST':
        answerForm = FormAnswer(data=request.POST)
        if answerForm.is_valid():
            answer = answerForm.save(commit=False)
            answer.academic = Academic.objects.get(user=request.user)
            answer.doubt = doubt
            answer.save()
            commented = True
    else:
        answerForm = FormAnswer()

    return render_to_response('baygon/doubt.html', {'doubt': doubt, 'answerForm': answerForm, 'commented': commented},
                              context_instance=RequestContext(request))