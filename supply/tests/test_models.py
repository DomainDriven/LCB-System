# -*- coding: utf-8 -*-
from datetime import datetime

from django.test import TestCase

from supply.models import Project, SalesBuy, FulfillmentCompany, Person


class ProjectTest(TestCase):
    def test_calculate_amount_of_order(self):
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
        amount_of_order = project.calculate_amount_of_order()

        # then
        self.assertEqual(amount_of_order, 100)

    def test_get_fulfillment_companies(self):
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
        FulfillmentCompany.objects.create(name=u'앤사', project=project)
        FulfillmentCompany.objects.create(name=u'비사', project=project)

        # when
        fulfillment_companies = project.get_fulfillment_companies()
        self.assertEqual(len(fulfillment_companies), 3)
        self.assertEqual(fulfillment_companies[0], u'앤사')
        self.assertEqual(fulfillment_companies[1], u'비사')
        self.assertEqual(fulfillment_companies[2], u'당사')

    def test_get_participants(self):
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

        project.participants.add(Person.objects.create(name=u'김아무'))
        project.participants.add(Person.objects.create(name=u'철수'))

        # when
        participants = project.get_participants()

        self.assertEqual(len(participants), 2)
        self.assertEqual(participants[0], u'김아무')
        self.assertEqual(participants[1], u'철수')


class SalesBuyTest(TestCase):
    def test_calculate_amount(self):
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
        sales_buy = SalesBuy.objects.create(year='2015', amount=46359176, project=project)

        # then
        self.assertEqual(sales_buy.calculate_amount(), 46)


class ProjectAndPersonTest(TestCase):
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

        person1 = Person.objects.create(name=u'김아무')
        person2 = Person.objects.create(name=u'철수')

        # when
        project.participants.add(person1)
        project.participants.add(person2)

        # then
        self.assertIn(person1, project.participants.all())
        self.assertIn(person2, project.participants.all())


class ProjectAndSalesBuyTest(TestCase):
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


class ProjectAndFulfillmentCompanyTest(TestCase):
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