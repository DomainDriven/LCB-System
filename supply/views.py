# -*- coding: utf-8 -*-
from django.shortcuts import render
from easydict import EasyDict as edict

from supply.models import Project


def home_page(request):
    return render(request, 'home.html')


def view_supply(request, project_no):
    project = Project.objects.get(project_no=project_no)

    project_supply = {
        'project_no': project.project_no,
        'customer': project.customer,
        'project_abbreviations': project.abbreviations,
        'fulfillment_companies': project.get_fulfillment_companies(),
        'contract_start_date': project.contract_start_date,
        'contract_end_date': project.contract_end_date,
        'amount_of_order': project.calculate_amount_of_order(),
        'sales_buy': {
            '2015': 46,
            '2016': 0,
            '2017': 0
        },
        'participants': [u'김아무', u'김아무'],
        'categories': [u'분1', '', ''],
        'representative': project.order_company_representative
    }

    return render(request, 'supply.html', context={'project_supply': edict(project_supply)})