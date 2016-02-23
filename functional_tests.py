# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver


class ProjectSupplyTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="webdriver\\chromedriver")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_retrieve_supply(self):
        """
        수행 과제 공급표 조회
        """
        # Kai 는 수행 과제에 대한 공급표를 조회 하기 위해 '예실 대비' 웹 사이트를 방문 한다.
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀에 '예실 대비'를 표시 하고 있다.
        self.assertEqual(self.browser.title, u'예실 대비')

        # 웹 사이트는 수행 과제 번호를 입력할 수 있는 입력 상자와 공급표를 조회할 수 있는 버튼을 재공 하고 있다.
        input_project_no = self.browser.find_element_by_id('project_no')
        button_retrieve_project_supply = self.browser.find_element_by_id('retrieve_project_supply')

        self.assertIsNotNone(input_project_no)
        self.assertIsNotNone(button_retrieve_project_supply)

        # Beck은 수행 과제 번호(0000)를 입력한다
        # 그리고 Beck은  '공급표 조회' 버튼을 누른다.
        # 수행 과제 번호에 해당하는 공급표가 보인다.