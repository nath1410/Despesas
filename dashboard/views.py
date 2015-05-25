# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def index(request):
           return render(request, 'index.html')

def config(request):
	return render(request, 'config.html')

def conta(request):
	return render(request, 'conta.html')

def ajuda(request):
	return render(request, 'ajuda.html')