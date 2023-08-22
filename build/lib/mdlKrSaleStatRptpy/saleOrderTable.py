#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyrda.dbms.rds import RdClient
import pandas as pd
def sql_query(token,FStartDate,FEndDate,FIsFree,FStatus,FBIllType,FOrgNumber):
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

    app3 = RdClient(token=token)

    sql=f"""
    SELECT          
	  '{FStartDate}' AS FStartDate,'{FEndDate}' AS FEndDate,           
	  row_number ( ) OVER ( ORDER BY  SUM (c.FAllAMOUNT_LC) desc) AS row_number,          
	  g.FNAME,          
	  f.FNUMBER AS FCustomerNumber,          
	  f.FNAME AS FCustomerName,          
	  SUM ( c.FALLAMOUNT ) AS FALLAMOUNT,          
	  SUM ( c.FAllAMOUNT_LC ) AS FAllAMOUNT_LC,          
	  e.FNAME AS FCurrencyName,          
	  y.FNAME as FMaterialType,        
	 CAST('{FIsFree}' as nvarchar) as FIsFree,        
	  CAST('{FStatus}' as nvarchar) as FSTatus        
		FROM          
	  T_SAL_ORDER a          
	   inner join T_SAL_ORDERENTRY b            
	   on a.FID=b.FID            
	   inner join T_SAL_ORDERENTRY_F c            
	   on c.FID=a.FID   and b.FENTRYID = c.FENTRYID          
	   inner join T_SAL_ORDERFIN d            
	   on a.FID=d.FID            
	   inner join rds_vw_currency e            
	   on e.FCURRENCYID=d.FSETTLECURRID           
	   inner join rds_vw_customer f            
	   on f.FCUSTID=a.FCUSTID            
	   inner join rds_vw_organization g            
	   on g.FORGID=a.FSALEORGID            
	   inner join T_BD_MATERIAL h            
	   on h.FMATERIALID=b.FMATERIALID            
	   inner join rds_vw_billtype y            
	   on y.FBILLTYPEID=a.FBILLTYPEID          
	   WHERE          
	  convert(nvarchar(20),a.FAPPROVEDATE,23)>='{FStartDate}'           
	  AND convert(nvarchar(20),a.FAPPROVEDATE,23)<='{FEndDate}'          
	  AND (1 = (CASE WHEN  '全部'='{FStatus}' THEN 1 ELSE 0 END) OR (a.FDOCUMENTSTATUS !=(CASE WHEN '未审核'='{FStatus}' THEN 'C' END)) OR (a.FDOCUMENTSTATUS =(CASE WHEN '已审核'='{FStatus}' THEN 'C' END)))          
	  AND  y.FNAME in ({FBIllType})  
	  AND  g.FNumber  in ({FOrgNumber})
	  and (1 = (CASE WHEN '是' ='{FIsFree}' THEN 1 ELSE 0 END) OR c.FISFREE = '0')          
	   group by g.FNAME,f.FNAME,e.FNAME,y.FNAME ,f.FNUMBER
    """
    res=app3.select(sql)

    df=pd.DataFrame(res)

    return df

