# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from easydict import EasyDict as edict


def home_page(request):
    return render(request, 'home.html')


def view_supply(request, project_no):
    project_supply = {
        'project_no': project_no,
        'customer': u'에스사',
        'project_abbreviations': u'정보계',
        'fulfillment_companies': [u'앤사', u'당사'],
        'contract_start_date': '14/02/01',
        'contract_end_date': '15/03/20',
        'amount_of_order': 100,
        'sales_buy': {
            '2015': 46,
            '2016': 0,
            '2017': 0
        },
        'participants': [u'김아무', u'김아무'],
        'categories': [u'분1', '', ''],
        'representative': u'이아무'
    }

    return render(request, 'supply.html', context={'project_supply': edict(project_supply)})