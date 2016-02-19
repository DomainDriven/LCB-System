# -*- coding: utf-8 -*-
from datetime import datetime

from django.test import TestCase

from supply.models import Project, Employee, SalesBuy


class ProjectTest(TestCase):
    def test_save_and_retrieve(self):
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
        actual = Project.objects.get(project_no=project.project_no)

        # then
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(project, actual)


class ProjectAndEmployee(TestCase):
    def test_save_and_retrieve(self):
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
        Employee.objects.create(name=u'김아무', project=project)
        Employee.objects.create(name=u'김아무2', project=project)

        # when
        actual_employees = Employee.objects.filter(project__project_no=project.project_no)

        # then
        self.assertEqual(len(actual_employees), 2)


class ProjectAndSalesBuy(TestCase):
    def test_save_and_retrieve(self):
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

        SalesBuy.objects.create(year='2014', amount=149640833, project=project)
        SalesBuy.objects.create(year='2015', amount=46359176, project=project)

        # when
        actual_sales_buy = SalesBuy.objects.filter(project__project_no=project.project_no)

        # then
        self.assertEqual(len(actual_sales_buy), 2)