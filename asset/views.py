# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import CUSTOMER,DEV,STORE
from django.utils import timezone
# Create your views here.
from django.contrib.auth.decorators import login_required
import zmq
addr = 'tcp://127.0.0.1:5555'
con = zmq.Context()
push = con.socket(zmq.PUSH)
push.connect(addr)
push.send_unicode(u"Django runing")
class LoginRequiredMixin(object):
    """
    登陆限定，并指定登陆url
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/admin/')
class IndexView(LoginRequiredMixin,generic.ListView):
    template_name = 'asset/index.html'
    context_object_name = 'dev_sets'
    def get_queryset(self):

        return DEV.objects.all()

class DevInfoView(LoginRequiredMixin,generic.DetailView):
    model = DEV
    template_name = 'asset/dev_info.html'
    def get_queryset(self):
        push.send_json({ "name":DEV.objects.all()[0].node_name})
        return DEV.objects.all()