# -*- coding: utf-8 -*-
from django.test import TestCase


class HomeViewTest(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ProjectSupplyViewTest(TestCase):
    def test_use_supply_template(self):
        response = self.client.get('/project/0000/supply/')
        self.assertTemplateUsed(response, 'supply.html')