import initConstant as ic
def countInTime(recordWithID):
    #recordWithID is a dictionary form in <ID,<timeDim,<function,times>>>
    timeRecord = dict()
    for eachID in recordWithID:
        tmp_timeRecord = recordWithID[eachID]
        for eachtime in tmp_timeRecord:
            tmp_functionRecord = tmp_timeRecord[eachtime]
            if eachtime in timeRecord:
                for eachfunction in ic.functionlist:
                    timeRecord[eachtime][eachfunction] = timeRecord[eachtime][eachfunction] + tmp_functionRecord[eachfunction]
            else: 
                timeRecord[eachtime] = tmp_functionRecord
    return timeRecord
