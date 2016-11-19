# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:19:27 2016

@author: claude
"""

import tushare as ts
import datetime
import time
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine
import multiprocessing

from config import *
#engine = create_engine('mysql://duser:1qaz@WSX@106.14.42.175/darkhorse?charset=utf8')
    
def GetDbValue(conn,sql):
    """
    SQL to dataframe
    """
    try:
        return pd.read_sql(sql,conn);
    except IOError:
        return None   
        
def GetValue(number):
    """
    string to float
    """
    try:
        return float(number)
    except ValueError:
        return 0

def GetFormatNowTime():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def GetFormatdatetime(date,time):
    return date[0:4]+date[5:7]+date[8:10]+time[0:2]+time[3:5]+time[6:8]
        
def deco(func):
    def _deco(*args, **kwargs):
        print "Begin",
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        print otherStyleTime
        res = func(*args, **kwargs)
        time.sleep(5)
        return  res
    return _deco        
        
