# -*- encoding: utf-8 -*-
#!/usr/bin/env python2.7

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from baygon.models import Doubt, Answer

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