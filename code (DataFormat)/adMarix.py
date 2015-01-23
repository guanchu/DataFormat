# -*- coding: utf-8 -*-
from Minkowski import minkowski
from EditDistance import EditDistance
from editCode import editCode
from timeDimention import userRecord
from countInFunction import countInFunction
import time
import initConstant as ic
def adMarix(record,distanceType,timDim,p = 0):
    #record is a dictionary formed in <A,<B,times>>
    #the adMarix is used to perform the graph which has two dimensions and a number
    #这里的逻辑就是首先A和OtherA是同一个list中的内容，但是A中的B和OtherA中的OtherB是会不同的
    matrix = dict()
    if (distanceType == 'minkowDis') and (p != 0):
        t = 0
        for eachA in record:
            t += 1
            print '已处理'+repr(t)+"/16，当前时间为："
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            tmp_Brecord = record[eachA]
            tmp_dic = dict() 
            for otherA in record:
                tmp_otherBRecord = record[otherA]
                distance = minkowski(timDim,tmp_Brecord,tmp_otherBRecord,p)
                tmp_dic[otherA] = distance
            matrix[eachA] = tmp_dic
    elif distanceType == 'editDis':
        print record
        
        editCodeMatrix = editCode(record,timDim)

        t = 0
        print editCodeMatrix
        for eachfunction in editCodeMatrix:
            t += 1
            #print '已处理'+repr(t)+"/30，当前时间为："
            
            tmp_function = editCodeMatrix[eachfunction]
            str1 = ''.join(tmp_function)
           
            tmp_dic = dict()
            for otherfunction in editCodeMatrix:
                temp_function = editCodeMatrix[otherfunction]
                str2 = ''.join(temp_function)  
                arith = EditDistance()             
                tmp_dic[otherfunction] = arith.levenshtein(str1,str2)               
            matrix[eachfunction] = tmp_dic
            #print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return matrix
