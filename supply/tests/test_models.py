# -*- coding: utf-8 -*-
from datetime import datetime

from django.test import TestCase

from supply.models import Project, Employee, SalesBuy, FulfillmentCompany


class ProjectAndEmployee(TestCase):
    def test_related_item(self):
        # given
        project = Project.objects.create(project_no='0000',
                                         customer=u'에스사',
                                         abbreviations=u'정보계',
                                         contract_name=u'정보계 개선',
                                         contract_start_date=datetime(year=2014, month=2, day=1),
                                         contract_end_date=datetime(year=2015, month=3, day=20),
                                         order_company=u'앤사',
                                         order_company_representative=u'이아무',
                                         amount_of_order=100000000,
                                         amount_of_order_type='SI',
                                         category1=u'분1')

        # when
        emp1 = Employee.objects.create(name=u'김아무', project=project)
        emp2 = Employee.objects.create(name=u'김아무2', project=project)

        # then
        self.assertIn(emp1, project.employee_set.all())
        self.assertIn(emp2, project.employee_set.all())


class ProjectAndSalesBuy(TestCase):
    def test_related_item(self):
        # given
        project = Project.objects.create(project_no='0000',
                                         customer=u'에스사',
                                         abbreviations=u'정보계',
                                         contract_name=u'정보계 개선',
                                         contract_start_date=datetime(year=2014, month=2, day=1),
                                         contract_end_date=datetime(year=2015, month=3, day=20),
                                         order_company=u'앤사',
                                         order_company_representative=u'이아무',
                                         amount_of_order=100000000,
                                         amount_of_order_type='SI',
                                         category1=u'분1')

        # when
        sales_buy_1 = SalesBuy.objects.create(year='2014', amount=149640833, project=project)
        sales_buy_2 = SalesBuy.objects.create(year='2015', amount=46359176, project=project)

        # then
        self.assertIn(sales_buy_1, project.salesbuy_set.all())
        self.assertIn(sales_buy_2, project.salesbuy_set.all())


class ProjectAndFulfillmentCompany(TestCase):
    def test_related_item(self):
        # given
        project = Project.objects.create(project_no='0000',
                                         customer=u'에스사',
                                         abbreviations=u'정보계',
                                         contract_name=u'정보계 개선',
                                         contract_start_date=datetime(year=2014, month=2, day=1),
                                         contract_end_date=datetime(year=2015, month=3, day=20),
                                         order_company=u'앤사',
                                         order_company_representative=u'이아무',
                                         amount_of_order=100000000,
                                         amount_of_order_type='SI',
                                         category1=u'분1')

        # when
        fulfillment_company = FulfillmentCompany.objects.create(name=u'앤사', project=project)

        # then
        self.assertIn(fulfillment_company, project.fulfillmentcompany_set.all())