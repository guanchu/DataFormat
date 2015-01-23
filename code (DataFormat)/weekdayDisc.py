from  datetime  import  *  
import  time 
import string
def weekdayDisc(str):
    #return a contant number that is a index in weekdaylist
    tmp =str.split('-')
    year = string.atoi(tmp[0])
    month = string.atoi(tmp[1])
    day = string.atoi(tmp[2])
    datetime = date( year ,  month ,  day ) 
    return datetime.weekday()

#print weekdayDisc('2013-08-10')