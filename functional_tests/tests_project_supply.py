# -*- coding: utf-8 -*-
import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class ProjectSupplyTest(StaticLiveServerTestCase):
    fixtures = ['supply/tests/test_fixture/supply.json']

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=os.path.dirname(os.path.abspath(__file__)) + '\\webdriver\\chromedriver.exe')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_can_retrieve_project_supply(self):
        """
        수행 과제 공급표 조회
        """
        # 철수는 수행 과제에 대한 공급표를 조회 하기 위해 '예실 대비' 웹 사이트를 방문 한다.
        self.browser.get(self.live_server_url)

        # 웹 페이지 타이틀에 '예실 대비'를 표시 하고 있다.
        self.assertEqual(self.browser.title, u'예실 대비')

        # 웹 사이트는 수행 과제 번호를 입력할 수 있는 입력 상자와 공급표를 조회할 수 있는 버튼을 재공 하고 있다.
        input_project_no = self.browser.find_element_by_id('project_no')
        button_retrieve_project_supply = self.browser.find_element_by_id('retrieve_project_supply')

        self.assertIsNotNone(input_project_no)
        self.assertIsNotNone(button_retrieve_project_supply)

        # 철수는 수행 과제 번호(0000)를 입력한다
        input_project_no.send_keys('0000')
        # 그리고 철수는  '공급표 조회' 버튼을 누른다.
        button_retrieve_project_supply.click()

        # 수행 과제 번호에 해당하는 공급표가 보인다.
        self.assertEqual(self.browser.find_element_by_css_selector('.page-header').text, u'과제 공급표')
        supply_tr_list = self.browser.find_element_by_css_selector('.sensei-grid-tbody').find_elements_by_tag_name('tr')
        self.assertEqual(len(supply_tr_list), 1)

        # # 과제 번호
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[0].find_element_by_tag_name('div').text,
                         '0000')
        # # 고객(갑)
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[1].find_element_by_tag_name('div').text,
                         u'에스사')
        # # 과제 약칭
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[2].find_element_by_tag_name('div').text,
                         u'정보계')
        # # 을_병_정_무
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[3].find_element_by_tag_name('div').text,
                         u'앤사>당사')
        # # 계약 기한
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[4].find_element_by_tag_name('div').text,
                         u'14/02/01~15/03/20')
        # # 수주액
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[5].find_element_by_tag_name('div').text,
                         '100')
        # # 매출(2015, 2016, 2017)
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[6].find_element_by_tag_name('div').text,
                         '46')
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[7].find_element_by_tag_name('div').text,
                         '0')
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[8].find_element_by_tag_name('div').text,
                         '0')
        # # 참여자
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[9].find_element_by_tag_name('div').text,
                         u'김아무 홍길동')
        # # 분류1,2,3
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[10].find_element_by_tag_name('div').text,
                         u'분1')
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[11].find_element_by_tag_name('div').text,
                         u'')
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[12].find_element_by_tag_name('div').text,
                         u'')
        # # 대표자
        self.assertEqual(supply_tr_list[0].find_elements_by_tag_name('td')[13].find_element_by_tag_name('div').text,
                         u'이아무')