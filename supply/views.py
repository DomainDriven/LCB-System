# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def view_supply(request, proejct_no):
    return render(request, 'supply.html')