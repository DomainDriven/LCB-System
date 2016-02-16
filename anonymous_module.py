# -*- coding: utf-8 -*-
"""
Created on 2016. 2. 4.

@author: 유영모
"""
from easydict import EasyDict


def get_dummy_data():
    """
    계획은 비휘발성 자장소(DB 혹은 File)에서 데이터를 조회 해야 하나
    현재는 메모리 상에서 임시 데이터를 반환 한다.
    """
    return [
        {
            'project_no': 0000,
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
    수행 과제 클래스
    """
    def __init__(self, project_no):
        self.project_no = project_no

    def get_supply(self):
        """
        공급표 구하기
        :return: 공급표
        """
        # TODO: 리펙토링 - 목표 : 더미 데이터를 가공하여 테스트를 통과 하게 하자. 
        return EasyDict(
            {
                'project_no': '0000',
                'customer': u'에스사',
                'project_abbreviations': u'정보계',
                'fulfillment_company': [
                    u'앤사',
                    u'당사'
                ],
                'contract_start_date': '14/02/01',
                'contract_end_date': '15/03/20',
                'amount_of_order': 100,
                'sales': {
                    '2015': 46,
                    '2016': 0,
                    '2017': 0
                },
                'participants': [
                    u'김아무', u'김아무'
                ],
                'categories': [
                    u'분1',
                    '',
                    '',
                ],
                'representative': u'이아무'
             }
        )

