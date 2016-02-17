# -*- coding: utf-8 -*-
"""
Created on 2016. 2. 4.

@author: 유영모
"""
import datetime
from time import strptime, strftime

from easydict import EasyDict


def get_dummy_data():
    """
    계획은 비휘발성 자장소(DB 혹은 File)에서 데이터를 조회 해야 하나
    현재는 메모리 상에서 임시 데이터를 반환 한다.
    """
    return [
        {
            'project_no': '0000',
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
                'commitment_end_date': '2015-03-20',
                'commitment_resource': [
                    u'김아무', u'김아무'
                ],
                'category1': u'분1',
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
        # TODO: '함수는 한 가지만 해야 한다' 준수 하기 - From Clean Code
        # TODO: '매직 숫자는 명명된 상수로 교체 하라' 준수 하기 - From Clean Code
        project = [data for data in get_dummy_data() if data['project_no'] == '0000']
        if len(project) == 1:
            project_no = project[0]['project_no']
            customer = project[0]['project_summary']['customer']
            project_abbreviations = project[0]['project_summary']['abbreviations']

            # =CONCATENATE(D71&"> "&"당사")
            fulfillment_company = [project[0]['project_summary']['order_company'], u'당사']

            # =TEXT($G$71,"yy/mm/dd")&"~"&TEXT($H$71,"yy/mm/dd")
            contract_start_date = strftime('%y/%m/%d',
                                           strptime(project[0]['project_summary']['contract_start_date'], '%Y-%m-%d'))
            contract_end_date = strftime('%y/%m/%d',
                                         strptime(project[0]['project_summary']['contract_end_date'], '%Y-%m-%d'))
            # =IFERROR(D72/1000000,"")
            amount_of_order = project[0]['project_summary']['amount_of_order'] / 1000000

            # =IFERROR(INDEX($E$51:$H$51,MATCH(I$4,$E$50:$H$50,0))/1000000,"")
            sales = {
                '2015': project[0]['sales_buy']['2015'] / 1000000,
                '2016': project[0]['sales_buy']['2016'] / 1000000,
                '2017': project[0]['sales_buy']['2017'] / 1000000,
            }

            # =CONCATENATE(G73," ",H73)
            participants = project[0]['project_summary']['commitment_resource']

            # =IF(ISNUMBER(FIND("분류",$O$71,1)),"",$O$71)
            categories = [project[0]['project_summary']['category1'],
                          project[0]['project_summary']['category2'],
                          project[0]['project_summary']['category3']]

            representative = project[0]['project_summary']['order_company_representative']

            return EasyDict(
                {
                    'project_no': project_no,
                    'customer': customer,
                    'project_abbreviations': project_abbreviations,
                    'fulfillment_company': fulfillment_company,
                    'contract_start_date': contract_start_date,
                    'contract_end_date': contract_end_date,
                    'amount_of_order': amount_of_order,
                    'sales': sales,
                    'participants': participants,
                    'categories': categories,
                    'representative': representative
                 }
            )








