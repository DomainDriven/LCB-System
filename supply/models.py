# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Project(models.Model):
    """
    수행 과제
    """
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

    # def get_fulfillment_companies(self):
    #     pass


class Employee(models.Model):
    """
    직원
    """
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project)


class SalesBuy(models.Model):
    """
    매출입/과총
    """
    year = models.CharField(max_length=4)
    amount = models.BigIntegerField()
    project = models.ForeignKey(Project)


class FulfillmentCompany(models.Model):
    """
    수행사
    """
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project)