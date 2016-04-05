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
            '2015': project.salesbuy_set.get(year='2015').calculate_amount(),
            '2016': project.salesbuy_set.get(year='2016').calculate_amount(),
            '2017': project.salesbuy_set.get(year='2017').calculate_amount()
        },
        'participants': project.get_participants(),
        'category1': project.category1,
        'category2': project.category2,
        'category3': project.category3,
        'representative': project.order_company_representative
    }

    return render(request, 'supply.html', context={'project_supply': edict(project_supply)})