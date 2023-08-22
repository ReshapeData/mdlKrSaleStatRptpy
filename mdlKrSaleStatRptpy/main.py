#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .saleOrderTable import *
def saleOrderTable_query(token,FStartDate,FEndDate,FIsFree,FStatus,FBIllType,FOrgNumber):
    '''
    凯润销售订单统计表查询
    :param token: ERP数据库token
    :param FStartDate: 开始时间
    :param FEndDate: 结束时间
    :param FIsFree: 是否赠品
    :param FStatus: 状态
    :param FBIllType: 单据类型
    :param FOrgNumber: 组织编码
    :return:
    '''

    res=sql_query(token,FStartDate,FEndDate,FIsFree,FStatus,FBIllType,FOrgNumber)

    return res
