#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdlKrSaleStatRptpy import *

res=saleOrderTable_query(token="B3455A86-2376-4EF3-8000-39AA8B61B759",
                         FStartDate="2023-08-01",FEndDate="2023-08-22",FIsFree="否",FStatus="全部",FBIllType="'标准销售订单','样品销售订单'",
                         FOrgNumber="102")

print(res)