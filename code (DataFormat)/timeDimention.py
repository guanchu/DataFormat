#!/user/bin/env python
# -*- coding: utf-8 -*-
from weekdayDisc import weekdayDisc
import initConstant as ic
def userRecord(filepath,timeDim,userIDlist):
    #discover the choosen user' information
    #default users are all users
    #initialization
   
   
    outputResult = dict()
    fin = open(filepath, 'r')
    if fin:
        print 'open successfully'
    else:
        print 'wrong filepath'
        return
    for eachline in fin:
        (uid, time, func) = eachline.split('\t')
        ID = uid
        if ID in userIDlist:
            func = func.strip()
            month = time[0:7]
            day = time[8:10]+"d"
            weekdayIndex = weekdayDisc(time[0:10])
            week = ic.weeklist[weekdayIndex]
            hour = time[11:13]+"h" 
            if timeDim == "weekday":
                tempTime = week+":"+hour               
            if timeDim == "month":
                tempTime = day+":"+hour           
            if timeDim =="day":
                tempTime = hour               
            if timeDim == "all":
                tempTime = month+":"+day+":"+hour
        
            #只要有上一级，就有下一级的定义

            if ID in outputResult:
                timeFunctionRecord = outputResult[ID]
                if tempTime in timeFunctionRecord:
                    functionRecord = timeFunctionRecord[tempTime]
                    if func in functionRecord:
                        functionRecord[func] = functionRecord[func]+1
                    else:
                        functionRecord[func] = 1
                        timeFunctionRecord[tempTime] = functionRecord
                        outputResult[ID] = timeFunctionRecord
                else:
                    functionRecord = dict()
                    functionRecord[func] = 1
                    timeFunctionRecord[tempTime] = functionRecord
                    outputResult[ID] = timeFunctionRecord
            else:
                timeFunctionRecord = dict()
                functionRecord = dict()
                functionRecord[func] = 1
                timeFunctionRecord[tempTime] = functionRecord
                outputResult[ID] = timeFunctionRecord

    return outputResult
    fin.close()
