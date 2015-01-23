#!/user/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from math import sqrt
import initConstant as ic
import time
def minkowski(timeDim,B,otherB,r):
    #输入两个长度相同的字符串，并输入p值
    sum = 0
    t=0

    for eachB in  B:
        print '已处理',repr(t),"/30，当前时间为："
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        temp_Btime = B[eachB]
        if eachB in otherB:
            temp_otherBtime = otherB[eachB]
            sum = sum + pow(abs(temp_Btime-temp_otherBtime),r)
        else:
            sum = sum + pow(abs(temp_Btime-0),r)
    for eachOtherB in otherB:
        if eachOtherB in B:
            continue
        else:
            sum = sum + pow(abs(otherB[eachOtherB]-0),r)
    return pow(sum,1/r)
