# -*- coding: utf-8 -*-
import unittest
   
  
class TaskTest(unittest.TestCase):
      
    # 과제 목록 공급표 구하기
    def test_get_supply(self):
        task = Task(task_no='0000')
         
        supply = task.get_supply()
        self.assertEqual(supply.customer, u'에스사')
        self.assertEqual(supply.abbreviations, u'정보계')
        self.assertEqual(supply.contractor, u'앤사> 당사')
        self.assertEqual(supply.abbreviations, u'정보계')
        self.assertEqual(supply.contract_date, '14/02/01~15/03/20')
        self.assertEqual(supply.amount_of_order, 100)
        self.assertEqual(supply.this_year, 46)
        self.assertEqual(supply.next_year, 0)
        self.assertEqual(supply.three_years_from_now, 0)
        self.assertEqual(supply.participants, u'김아무 김아무')
        self.assertEqual(supply.category1, u'분1')
        self.assertEqual(supply.category2, u'')
        self.assertEqual(supply.category3, u'')
        self.assertEqual(supply.representative, u'이아무')
          
          
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()