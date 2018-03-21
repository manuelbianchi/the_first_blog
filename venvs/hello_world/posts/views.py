# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def lista_post(request):
    return render(request, "lista_post.html")

def post_singolo(request):
    return render(request, "post_singolo.html")

def contatti(request):
    return render(request, "contatti.html")