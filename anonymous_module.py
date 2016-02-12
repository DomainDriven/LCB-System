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
    return [
        {
            'project_id': 0000,
            'project_summary': {
                'customer':  u'에스사',
                'abbreviations': u'정보계',
                'contract_name': u'정보계 개선',
                'order_company': u'앤사',
                'order_company_representative': u'이아무',
                'amount_of_order': 100000000,
                'amount_of_order_type': 'SI',
                'contract_start_date': '2014-02-01',
                'contract_end_date': '2015-03-20',
                'commitment_start_date': '2014-02-01',
                'commitment_start_date': '2015-03-20',
                'commitment_resource': [
                    '김아무', '김아무'
                ],
                'category1':'분1',
                'category2':'',
                'category3':'',
            },
            'sales_buy': {
                '2014': 149640833,
                '2015': 46359176,
                '2016': 0,
                '2017': 0,
            },
        },
    ]


class Project:
    """
    '과제'를
    """
    def __init__(self):
        pass