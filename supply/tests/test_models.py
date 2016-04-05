# -*- coding: utf-8 -*-
from datetime import datetime

from django.test import TestCase

from supply.models import Project, SalesBuy, FulfillmentCompany, Person


class ProjectTest(TestCase):
    fixtures = ['supply/tests/test_fixture/supply.json']

    def test_calculate_amount_of_order(self):
        # given
        project = Project.objects.get(project_no='0000')

        # when
        amount_of_order = project.calculate_amount_of_order()

        # then
        self.assertEqual(amount_of_order, 100)

    def test_get_fulfillment_companies(self):
        # given
        project = Project.objects.get(project_no='0000')
        FulfillmentCompany.objects.create(name=u'비사', project=project)

        # when
        fulfillment_companies = project.get_fulfillment_companies()
        self.assertEqual(len(fulfillment_companies), 3)
        self.assertEqual(fulfillment_companies[0], u'앤사')
        self.assertEqual(fulfillment_companies[1], u'비사')
        self.assertEqual(fulfillment_companies[2], u'당사')

    def test_get_participants(self):
        # given
        project = Project.objects.get(project_no='0000')

        # when
        participants = project.get_participants()

        self.assertEqual(len(participants), 2)
        self.assertEqual(participants[0], u'김아무')
        self.assertEqual(participants[1], u'홍길동')


class SalesBuyTest(TestCase):
    fixtures = ['supply/tests/test_fixture/supply.json']

    def test_calculate_amount(self):
        # given
        sales_buy = SalesBuy.objects.get(id=1)

        # when
        amount = sales_buy.calculate_amount()

        # then
        self.assertEqual(amount, 46)


class ProjectAndPersonTest(TestCase):
    fixtures = ['supply/tests/test_fixture/supply.json']

    def test_related_item(self):
        # given
        project = Project.objects.get(project_no='0000')
        person1 = Person.objects.get(id=1)
        person2 = Person.objects.get(id=2)

        # when
        participants = project.participants.all()

        # then
        self.assertIn(person1, participants)
        self.assertIn(person2, participants)


class ProjectAndSalesBuyTest(TestCase):
    fixtures = ['supply/tests/test_fixture/supply.json']

    def test_related_item(self):
        # given
        project = Project.objects.get(project_no='0000')
        sales_buy_1 = SalesBuy.objects.get(id=1)
        sales_buy_2 = SalesBuy.objects.get(id=2)

        # when
        sales_buys = project.salesbuy_set.all()

        # then
        self.assertIn(sales_buy_1, sales_buys)
        self.assertIn(sales_buy_2, sales_buys)


class ProjectAndFulfillmentCompanyTest(TestCase):
    fixtures = ['supply/tests/test_fixture/supply.json']

    def test_related_item(self):
        # given
        project = Project.objects.get(project_no='0000')
        fulfillment_company = FulfillmentCompany.objects.get(id=1)

        # when
        companies = project.fulfillmentcompany_set.all()

        # then
        self.assertIn(fulfillment_company, companies)