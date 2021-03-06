#-*- encoding: utf-8 -*-
# input filepath
import sys
import initConstant as ic
from normalize import normalize
from Minkowski import minkowski
from EditDistance import EditDistance
from editCode import editCode
from timeDimention import userRecord
from adMarix import adMarix
from countInFunction import countInFunction
from countUserNum import countUserNum
#from draw import draw
user = raw_input("请输入用户来源（yudian or lingxi）: ")
filepath = raw_input("请输入文件所在路径: ")
fin = open(filepath, 'r')
if fin:
        print '文件路径为：',filepath
        fin.close()
else:
        print '错误的文件路径'
        sys.exit(0)


#input timeDim
timeDim = raw_input("请输入需要统计的时间维度（all or weekday or month or day）:")
if (timeDim == 'all') or (timeDim == 'weekday') or (timeDim == 'month') or (timeDim == 'day') :
    print '时间维度为：',timeDim
else:
    print '错误的时间维度'
    sys.exit(0)

#input userlist(default is all lingxiUsers) and count with the conditions given
userrecord = dict()
inputuserlist = raw_input("请输入要查询的用户ID，以逗号分隔，或者直接输入default统计所有用户:")
userlist = list()
if inputuserlist == 'default':
    userlist = list()
    print '开始统计所有用户信息'
    if user == 'yudian':
        userlist = ic.yudianidlist
    elif user == 'lingxi':
        userlist = ic.lingxiidlist
    else:
        print '错误的用户信息'
        sys.exit(0)

    userrecord = userRecord(filepath,timeDim,userlist)
else:
    userlist = inputuserlist.split(',')
    print '用户列表为:',userlist
    print '开始统计这部分用户信息'
    userrecord = userRecord(filepath,timeDim,userlist)


#choose a distance computing formula
p = 0
typeofdistance = raw_input("请选择距离公式（editDis or minkowDis）: ")
if typeofdistance == 'minkowDis':
    p = input("请输入p值：")
    print '当前距离公式：',typeofdistance
    print 'p值为：',p
elif typeofdistance == 'editDis':
    print '当前距离公式：',typeofdistance
else:
    print '错误的距离公式'
    sys.exit(0)

#choose the dimension of vectors which will be computed for their distance
resultMarix = dict()
# countDim = raw_input("请输入要计算的向量维度(function or time):")
# countintime = dict()
#countinfunction = dict()
#if countDim == 'time':
#     print '以时间维度统计不同功能使用次数的向量'
#     print '统计中...'
#     countintime = countInTime(userrecord)
#     normaldecide = raw_input("是否归一化处理(y or n): ")
#    if normaldecide =='y':
#         normal_countintime = normalize(countintime)
#       resultMarix = adMarix(normal_countintime,typeofdistance,timeDim,p)
# elif normaldecide =='n':
#   resultMarix = adMarix(countintime,typeofdistance,timeDim,p)
#     else:
#         print 'wrong normalize parameter'
#         sys.exit(0)
# elif countDim == 'function':
typeofCount = raw_input("请选择要统计的类型（useTimes or userNum）: ")
if typeofCount == 'useTimes':
    print '以功能维度统计不同时间使用次数的向量'
    print '统计中...'
    countinfunction = countInFunction(userrecord)
    #drawDecide = raw_input("是否展示各功能随时间变化的图像(y or n): ")
    #if drawDecide == 'y':
    #   draw(countinfunction,timeDim)
    normaldecide = raw_input("是否归一化处理(y or n): ")
    if normaldecide =='y':
        normal_countinfunction = normalize(countinfunction)
        resultMarix = adMarix(normal_countinfunction,typeofdistance,timeDim,p)
    elif normaldecide =='n':
        resultMarix = adMarix(countinfunction,typeofdistance,timeDim,p)
    else:
        print 'wrong normalize parameter'
        sys.exit(0)
elif typeofCount == 'userNum':
    print '以功能维度统计不同时间用户数的向量'
    print '统计中...'
    countusernum = countUserNum(userrecord)
    #drawDecide = raw_input("是否展示各功能随时间变化的图像(y or n): ")
    #if drawDecide == 'y':
    #    draw(countusernum,timeDim)
    normaldecide = raw_input("是否归一化处理(y or n): ")
    if normaldecide =='y':
        normal_countusernum = normalize(countusernum)
        resultMarix = adMarix(normal_countusernum,typeofdistance,timeDim,p)
        print '已返回邻接矩阵'
    elif normaldecide =='n':
        resultMarix = adMarix(countusernum,typeofdistance,timeDim,p)
        print '已返回邻接矩阵'
    else:
        print 'wrong normalize parameter'
        sys.exit(0)

outputfilepath = raw_input('已做好邻接矩阵，请输入输出路径：')
fout = open(outputfilepath, 'w')
# print >> fout, 'count each business in every month'
functionOrder = resultMarix.keys()
for m in range(len(functionOrder)):
    fout.write('\t'+functionOrder[m])
fout.write('\n')
for i in range(len(functionOrder)):
    rowFunction = functionOrder[i]
    fout.write(rowFunction+'\t')
    for j in range(len(functionOrder)):
        colFunction = functionOrder[j]
        tempNum = resultMarix[rowFunction][colFunction]
        fout.write(colFunction+":"+repr(tempNum)+'\t')
    fout.write('\n')
fout.close()




