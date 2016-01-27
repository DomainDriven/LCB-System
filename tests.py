# -*- coding: utf-8 -*-
import unittest
__author__ = 'yooyoung-mo'


class TaskSupplyTest(unittest.TestCase):

    # 과제 목록 공급표 구하기
    def get_test_task_supply(self):
        supply = Supply()

        task_supply = supply.get(task_no='0000')
        self.assertEqual(task_supply.task_no, '0000')
        self.assertEqual(task_supply.customer, u'에스사')
        self.assertEqual(task_supply.abbreviations, u'정보계')
        self.assertEqual(task_supply.contractor, u'앤사> 당사')
        self.assertEqual(task_supply.abbreviations, u'정보계')
        self.assertEqual(task_supply.contract_date, '14/02/01~15/03/20')
        self.assertEqual(task_supply.amount_of_order, 100)
        self.assertEqual(task_supply.this_year, 46)
        self.assertEqual(task_supply.next_year, 0)
        self.assertEqual(task_supply.three_years_from_now, 0)
        self.assertEqual(task_supply.participants, u'김아무 김아무')
        self.assertEqual(task_supply.category1, u'분1')
        self.assertEqual(task_supply.category2, u'')
        self.assertEqual(task_supply.category3, u'')
        self.assertEqual(task_supply.representative, u'이아무')
