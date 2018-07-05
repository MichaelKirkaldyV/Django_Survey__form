# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request,'survey__form/index.html')

def submission(request):
	request.session['name'] = request.POST['name']
	request.session['locations'] = request.POST['locations']
	request.session['languages'] = request.POST['languages']
	request.session['comments'] = request.POST['comments']
	return redirect('/summary')

def summary(request):
	return render(request, 'survey__form/summary.html')
