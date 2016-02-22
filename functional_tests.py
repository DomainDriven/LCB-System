# -*- coding: utf-8 -*-
from django.test import LiveServerTestCase


class ProjectSupplyTest(LiveServerTestCase):
    def test_retrieve_supply(self):
        """
        수행 과제 공급표 조회
        """
        # Beck은 수행 과제에 대한 공급표를 조회 하기 위해 '예실 대비' 웹 사이트를 방문 한다.
        # 웹 사이트는 수행 과제 번호를 입력할 수 있는 입력 상자와 공급표를 조회할 수 있는 버튼을 재공 하고 있다.
        # Beck은 수행 과제 번호(0000)를 입력한다
        # 그리고 Beck은  '공급표 조회' 버튼을 누른다.
        # 수행 과제 번호에 해당하는 공급표가 보인다.