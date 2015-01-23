from timeDimention import userRecord
import initConstant as ic
def countUserNum(recordWithID):
    #it will return a <function,<timeDim,userlist>>
    functionRecord = dict()
    for eachID in recordWithID:
        tmp_timeRecord = recordWithID[eachID]
        for eachtime in tmp_timeRecord:
            tmp_function = tmp_timeRecord[eachtime]
            for eachfunction in tmp_function:
                if eachfunction in functionRecord:
                    temp_timeRecord = functionRecord[eachfunction]
                    if eachtime in temp_timeRecord:
                        temp_userlist = temp_timeRecord[eachtime]
                        if eachID in temp_userlist:
                            continue
                        else:
                            temp_userlist.append(eachID)
                            temp_timeRecord[eachtime] = temp_userlist
                            functionRecord[eachfunction] = temp_timeRecord
                    else:
                        temp_userlist = list()
                        temp_userlist.append(eachID)
                        temp_timeRecord[eachtime] = temp_userlist
                        functionRecord[eachfunction] = temp_timeRecord
                else:
                    temp_timeRecord = dict()
                    temp_userlist = list()
                    temp_userlist.append(eachID)
                    temp_timeRecord[eachtime] = temp_userlist
                    functionRecord[eachfunction] =temp_timeRecord
    outputRecord = dict()
    for eachfunction in functionRecord:
        tmp_timeRecord = functionRecord[eachfunction]
        output_timeRecord = dict()
        for eachtime in tmp_timeRecord:
            tmp_userlist = tmp_timeRecord[eachtime]
            tmp_num = len(tmp_userlist)
            output_timeRecord[eachtime] = tmp_num
        outputRecord[eachfunction] = output_timeRecord
    return outputRecord

    



