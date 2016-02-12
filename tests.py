# -*- coding: utf-8 -*-
import unittest


class Test(unittest.TestCase):
    # 과제 공급표 구하기
    def test_get_supply(self):
        # given. when
        # # 과제 조회 by 과제 번호
        project = Project.get(project_no='0000')
        # 조회한 과제의 공급표 조회
        project_supply = project.get_supply()

        # then
        # # 과제 번호
        self.assertEqual(project.project_id, '0000')
        # # 고객(갑)
        self.assertEqual(project_supply.customer.name, u'에스사')
        # # 과제 약칭
        self.assertEqual(project_supply.abbreviations, u'정보계')
        # # 을_병_정_무
        self.assertEqual(project_supply.contract.owner, u'앤사')
        self.assertEqual(project_supply.contract.contractor, u'당사')
        # # 계약 기한
        self.assertEqual(project_supply.contract.start_date, '14/02/01')
        self.assertEqual(project_supply.contract.end_date, '15/03/20')
        # # 수주액
        self.assertEqual(project_supply.amount_of_order, 100)
        # # 매출(2015, 2016, 2017)
        self.assertEqual(project_supply.sales['2015'], 46)
        self.assertEqual(project_supply.sales['2016'], 0)
        self.assertEqual(project_supply.sales['2017'], 0)
        # # 참여자
        self.assertEqual(project_supply.participants[0], u'김아무')
        self.assertEqual(project_supply.participants[1], u'김아무')
        # # 분류1,2,3
        self.assertEqual(project_supply.categories[0], u'분1')
        self.assertEqual(project_supply.categories[0], u'')
        self.assertEqual(project_supply.categories[2], u'')
        # # 대표자
        self.assertEqual(project_supply.representative, u'이아무')