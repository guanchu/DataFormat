# -*- coding: utf-8 -*- 
from pylab import *
import initConstant as ic
def draw(matrix,timeDim):
    #myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttf')
    #mpl.rcParams['axes.unicode_minus'] = False
    timelist = list()
    if timeDim == "weekday":
        timelist = ic.weekdaylist
                   
    if timeDim == "month":
        timelist = ic.monthlist  
             
    if timeDim =="day":
        timelist = ic.daylist 
                  
    if timeDim == "all":
        timelist = ic.alllist
    partNum = len(matrix)
    i = 0

    for eachRow in matrix:
        i += 1
        plt.subplot(partNum,1,i)
        
        tempDic = matrix[eachRow]
        changrow = dict()
        for eachtime in tempDic:
            tempindex = timelist.index(eachtime)
            tempnum = tempDic[eachtime]
            changrow[tempindex] = tempnum
        
        t = changrow.keys() 
        y = changrow.values()
        plt.plot(t, y)
        #plt.title(u,fontproperties=myfont) #指定字体
        plt.xlabel(u'time')
        plt.ylabel(u''+eachRow)
        plt.grid(True)
    plt.show()

record=dict()
temp1=dict()
temp2 = dict()
temp1['00h'] = 1
temp1['01h'] = 2
temp2['01h'] = 3
temp2['02h'] = 4
record['a'] = temp1
record['b'] = temp2
draw(record, 'day')