# -*- coding: utf-8 -*-
from timeDimention import userRecord
from countInFunction import countInFunction
import initConstant as ic

def editCode(matrix,timDim):
    timlist = list()
    outputMatrix_editCode = dict()
    if timDim == 'month':
        timlist = ic.monthlist
    elif timDim == 'day':
        timlist = ic.daylist
    elif timDim == 'all':
        timlist = ic.alllist
    elif timDim == 'weekday':
        timlist = ic.weekdaylist
    else:
        print 'wrong timDim'
        return 
    print '计算编辑距离中...'
    
    for eachfuntion in matrix:       
        tmp_timenum = matrix[eachfuntion]
        tmp_codeDic = list()
        for i in range(len(timlist)-1):
            timeAfter = timlist[i+1]
            timeBefor = timlist[i]
            timeAfterNum = 0
            timeBeforNum = 0
            if timeAfter in tmp_timenum:
                timeAfterNum = tmp_timenum[timeAfter]
            if timeBefor in tmp_timenum:
                timeBeforNum = tmp_timenum[timeBefor]
            if timeAfterNum>timeBeforNum :
                tmp_code = '1'
            else:
                tmp_code = '0'
            tmp_codeDic.append(tmp_code)
        outputMatrix_editCode[eachfuntion] = tmp_codeDic
    return outputMatrix_editCode

#record ={'contacts': {'09h': 1, '13h': 1, '16h': 1, '11h': 2, '14h': 1}, 'app': {'14h': 1}, 'restaurant': {'18h': 1}, 'telephone': {'10h': 55, '13h': 50, '16h': 59, '20h': 17, '17h': 81, '12h': 40, '18h': 50, '00h': 1, '11h': 47, '09h': 67, '01h': 2, '08h': 52, '19h': 16, '22h': 5, '15h': 43, '07h': 6, '23h': 2, '21h': 19, '14h': 59}, 'weather': {'10h': 1, '18h': 1, '14h': 1, '19h': 1}, 'dialog': {'10h': 1, '16h': 2, '18h': 5, '13h': 1, '11h': 2, '09h': 1, '19h': 2, '14h': 1}, 'message': {'23h': 2, '14h': 1}}
#print editCode(record,'day')
#filepath = "C:\Users\Administrator\Desktop\\testdata"
#ID = ic.yudianidlist
#output = userRecord(filepath,'day',ID)
#temp_matrix = countInFunction(output)
#output_matrix = editCode(temp_matrix,'day')
#print output_matrix['train']
