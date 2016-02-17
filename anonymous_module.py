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
    OUR_COMPANY = u'당사'
    DENOMINATOR = 1000000

    def __init__(self, project_no):
        self.project_no = project_no

    def get_project(self):
        projects = [data for data in get_dummy_data() if data['project_no'] == self.project_no]
        if len(projects) == 1:
            return projects[0]
        else:
            return None

    def get_supply(self):
        """
        공급표 구하기
        :return: 공급표
        """
        # TODO : 리펙토링 - __convert_date_string function을 Project 클래스에서 분리하기
        # TODO : 리펙토링 - DRY 원칙 지키기, 금액 계산 시 Project.DENOMINATOR로 나누고 있다. 이를 개선하자.
        project = self.get_project()

        project_no = project['project_no']
        customer = project['project_summary']['customer']
        project_abbreviations = project['project_summary']['abbreviations']

        # =CONCATENATE(D71&"> "&"당사")
        fulfillment_companies = self.__get_fulfillment_companies(project['project_summary']['order_company'])

        # =TEXT($G$71,"yy/mm/dd")&"~"&TEXT($H$71,"yy/mm/dd")
        contract_start_date = self.__convert_date_string(project['project_summary']['contract_start_date'],
                                                         '%Y-%m-%d', '%y/%m/%d')
        contract_end_date = self.__convert_date_string(project['project_summary']['contract_end_date'],
                                                       '%Y-%m-%d', '%y/%m/%d')

        # =IFERROR(D72/1000000,"")
        amount_of_order = self.__calculate_amount_of_order(project['project_summary']['amount_of_order'])

        # =IFERROR(INDEX($E$51:$H$51,MATCH(I$4,$E$50:$H$50,0))/1000000,"")
        sales_buy = self.__calculate_sales_buy(project['sales_buy'])

        # =CONCATENATE(G73," ",H73)
        participants = project['project_summary']['commitment_resource']

        # =IF(ISNUMBER(FIND("분류",$O$71,1)),"",$O$71)
        categories = [project['project_summary']['category1'],
                      project['project_summary']['category2'],
                      project['project_summary']['category3']]

        representative = project['project_summary']['order_company_representative']

        return EasyDict(
                {
                    'project_no': project_no,
                    'customer': customer,
                    'project_abbreviations': project_abbreviations,
                    'fulfillment_companies': fulfillment_companies,
                    'contract_start_date': contract_start_date,
                    'contract_end_date': contract_end_date,
                    'amount_of_order': amount_of_order,
                    'sales_buy': sales_buy,
                    'participants': participants,
                    'categories': categories,
                    'representative': representative
                }
        )

    @staticmethod
    def __get_fulfillment_companies(order_company):
        return [order_company, Project.OUR_COMPANY]

    @staticmethod
    def __convert_date_string(date_string, from_format, to_format):
        return strftime(to_format, strptime(date_string, from_format))

    @staticmethod
    def __calculate_amount_of_order(amount_of_order):
        return amount_of_order / Project.DENOMINATOR

    @staticmethod
    def __calculate_sales_buy(sales_buy):
        calculated_sales_buy = {}
        for key, value in sales_buy.iteritems():
            calculated_sales_buy.__setitem__(key, value / Project.DENOMINATOR)
        return calculated_sales_buy










