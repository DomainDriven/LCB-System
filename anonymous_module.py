# -*- coding: utf-8 -*-
"""
Created on 2016. 2. 4.

@author: 유영모
"""


def get_dummy_data():
    """
    계획은 비휘발성 자장소(DB 혹은 File)에서 데이터를 조회 해야 하나
    현재는 메모리 상에서 임시 데이터를 반환 한다.
    """
    return {
            'task_no': '0000',
            'task_summary': {
                               'customer': u'에스사',
                               'abbreviations': u'정보계',
                               'order_company': u'엔사',
                               'representative': u'이아무',
                               'contract_start_date': '2014-02-01',
                               'contract_end_date': '2015-03-20',
                               'amount_of_order': 100000000,
                               'amount_of_order_type': 'SI',
                               'in_personnel': ['김아무', '김아무'],
                               'category1': '분1',
                               'category2': '',
                               'category3': '',
                              },
            'sales': {
                       '2015': 46359176,
                       '2016': 0,
                       '2017': 0,
                       },
            }


class Task:
    """
    '과제'를
    """
    def __init__(self):
        pass