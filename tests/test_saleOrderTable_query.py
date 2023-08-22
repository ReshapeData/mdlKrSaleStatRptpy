#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdlKrSaleStatRptpy import *
import pytest


@pytest.mark.parametrize('token,FStartDate,FEndDate,FIsFree,FStatus,FBIllType,FOrgNumber,output',
                         [("B3455A86-2376-4EF3-8000-39AA8B61B759",
                         "2023-08-01","2023-08-22","否","全部","'标准销售订单','样品销售订单'","102", False)])

def test_saleOrderTable_query(token,FStartDate,FEndDate,FIsFree,FStatus,FBIllType,FOrgNumber,output):

    assert saleOrderTable_query(token,FStartDate,FEndDate,FIsFree,FStatus,FBIllType,FOrgNumber).empty == output
