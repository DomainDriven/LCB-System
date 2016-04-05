# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from time import strftime

from django.db import models
from django.utils.dateformat import DateFormat

ONE_MILLION_WON = 1000000


def express_one_million_won_unit(amount):
    """
    금액을 최소 백만원 단위로 표현 하여 반환 한다,
    :param amount: 금액
    :return: 백만원 단위 금액
    """
    return amount / ONE_MILLION_WON


class Person(models.Model):
    name = models.CharField(max_length=100)


class Project(models.Model):
    """
    수행 과제
    """
    OUR_COMPANY = u'당사'

    project_no = models.CharField(max_length=10, primary_key=True)
    customer = models.CharField(max_length=100)
    abbreviations = models.CharField(max_length=100)
    contract_name = models.CharField(max_length=100)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    order_company = models.CharField(max_length=100)
    order_company_representative = models.CharField(max_length=100)
    amount_of_order = models.BigIntegerField()
    amount_of_order_type = models.CharField(max_length=45)
    category1 = models.CharField(max_length=45)
    category2 = models.CharField(max_length=45)
    category3 = models.CharField(max_length=45)
    participants = models.ManyToManyField(Person)

    def calculate_amount_of_order(self):
        return express_one_million_won_unit(self.amount_of_order)

    def get_fulfillment_companies(self):
        result = []
        for company in self.fulfillmentcompany_set.all():
            result.append(company.name)
        result.append(self.OUR_COMPANY)
        return result

    def get_participants(self):
        result = []
        for participant in self.participants.all():
            result.append(participant.name)
        return result


class SalesBuy(models.Model):
    """
    매출입/과총
    """
    year = models.CharField(max_length=4)
    amount = models.BigIntegerField()
    project = models.ForeignKey(Project)

    def calculate_amount(self):
        return express_one_million_won_unit(self.amount)


class FulfillmentCompany(models.Model):
    """
    수행사
    """
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project)