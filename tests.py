# -*- coding: utf-8 -*-
import unittest


class TaskTest(unittest.TestCase):
    # 과제 목록 공급표 구하기
    def test_get_supply(self):
        task = Task.get(task_no='0000')
        self.assertEqual(task.abbreviations, u'정보계')
        # 공급
        supply = task.get_supply()
        self.assertEqual(supply.customer.name, u'에스사')
        self.assertEqual(supply.contract.owner, u'앤사')
        self.assertEqual(supply.contract.contractor, u'당사')
        self.assertEqual(supply.contract.start_date, '14/02/01')
        self.assertEqual(supply.contract.end_date, '15/03/20')
        self.assertEqual(supply.amount_of_order, 100)
        # 매출
        self.assertEqual(supply.sales.this_year, 46)
        self.assertEqual(supply.sales.next_year, 0)
        self.assertEqual(supply.sales.three_years_from_now, 0)
        # 과제 참여자
        self.assertEqual(supply.participants.length(), 2)
        self.assertEqual(supply.participants[0], u'김아무')
        self.assertEqual(supply.participants[1], u'김아무')
        # 분류
        self.assertEqual(supply.category.main, u'분1')
        self.assertEqual(supply.category.middle, u'')
        self.assertEqual(supply.category.sub, u'')
        self.assertEqual(supply.representative, u'이아무')
