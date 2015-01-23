from timeDimention import userRecord
import initConstant as ic
def countInFunction(recordWithID):
    functionRecord = dict()
    for eachID in recordWithID:
        tmp_timeRecord = recordWithID[eachID]
        for eachtime in tmp_timeRecord:
            tmp_funRecord = tmp_timeRecord[eachtime]
            for eachfunction in tmp_funRecord:
                tmp_times = tmp_funRecord[eachfunction]
                if eachfunction in functionRecord:
                    temp_timeDimTimes = functionRecord[eachfunction]
                    if eachtime in temp_timeDimTimes:
                        temp_timeDimTimes[eachtime] = temp_timeDimTimes[eachtime]+tmp_times
                        functionRecord[eachfunction] = temp_timeDimTimes
                    else:
                        temp_timeDimTimes[eachtime] = tmp_times
                        functionRecord[eachfunction] = temp_timeDimTimes
                else:
                    temp_timeDimTimes = dict()
                    temp_timeDimTimes[eachtime] = tmp_times
                    functionRecord[eachfunction] = temp_timeDimTimes
    return functionRecord
