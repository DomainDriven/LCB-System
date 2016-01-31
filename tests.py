# -*- coding: utf-8 -*-
import unittest
   
  
class TaskTest(unittest.TestCase):
      
    # 과제 목록 공급표 구하기
    def test_get_supply(self):
        task = Task.get(task_no='0000')
        self.assertEqual(task.abbreviations, u'정보계')
         
        supply = task.get_supply()   
        self.assertEqual(supply.customer.name, u'에스사')
        self.assertEqual(supply.contract.owner, u'앤사')
        self.assertEqual(supply.contract.contractor, u'당사')
        self.assertEqual(supply.contract.start_date, '14/02/01')
        self.assertEqual(supply.contract.end_date, '15/03/20')
        self.assertEqual(supply.amount_of_order, 100)
        self.assertEqual(supply.this_year, 46)
        self.assertEqual(supply.next_year, 0)
        self.assertEqual(supply.three_years_from_now, 0)
        self.assertEqual(supply.participants[0], u'김아무')
        self.assertEqual(supply.participants[2], u'김아무')
        self.assertEqual(supply.categories[0], u'분1')
        self.assertEqual(supply.categories[1], u'')
        self.assertEqual(supply.categories[2], u'')
        self.assertEqual(supply.representative, u'이아무')
          
          
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()