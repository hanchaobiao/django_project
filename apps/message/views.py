# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import request
from django.shortcuts import render

# Create your views here.


def getform(request):
    return render(request, 'message_form.html')
