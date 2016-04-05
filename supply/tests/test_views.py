# -*- coding: utf-8 -*-
import datetime
from django.test import TestCase


class HomeViewTest(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ProjectSupplyViewTest(TestCase):
    fixtures = ['supply/tests/test_fixture/supply.json']

    def test_use_supply_template(self):
        response = self.client.get('/project/0000/supply/')
        self.assertTemplateUsed(response, 'supply.html')

    def test_display_project_supply(self):
        # when
        response = self.client.get('/project/0000/supply/')
        actual = response.context['project_supply']

        # then
        # # 과제 번호
        self.assertEqual(actual.project_no, '0000')
        # # 고객(갑)
        self.assertEqual(actual.customer, u'에스사')
        # # 과제 약칭
        self.assertEqual(actual.project_abbreviations, u'정보계')
        # # 을_병_정_무
        self.assertEqual(actual.fulfillment_companies[0], u'앤사')
        self.assertEqual(actual.fulfillment_companies[1], u'당사')
        # # 계약 기한
        self.assertEqual(actual.contract_start_date, datetime.date(2014, 2, 1))
        self.assertEqual(actual.contract_end_date, datetime.date(2015, 3, 20))
        # # 수주액
        self.assertEqual(actual.amount_of_order, 100)
        # # 매출(2015, 2016, 2017)
        self.assertEqual(actual.sales_buy['2015'], 46)
        self.assertEqual(actual.sales_buy['2016'], 0)
        self.assertEqual(actual.sales_buy['2017'], 0)
        # # 참여자
        self.assertEqual(actual.participants[0], u'김아무')
        self.assertEqual(actual.participants[1], u'홍길동')
        # # 분류1,2,3
        self.assertEqual(actual.category1, u'분1')
        self.assertEqual(actual.category2, '')
        self.assertEqual(actual.category3, '')
        # # 대표자
        self.assertEqual(actual.representative, u'이아무')