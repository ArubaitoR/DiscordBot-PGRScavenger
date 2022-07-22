# PGR COOP
# 08:00am - 12:00 pm
# 04:00pm - 08:00pm
# 12:00am - 04:00am
import time

def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else:
        return nowTime >= startTime or nowTime <= endTime


#Jam Sekarang
timeNow = time.strftime("%H:%M", time.localtime())

#Jadwal Pertama
timeStart1 = '08:00'
timeEnd1 = '12:00'
result1 = isNowInTimePeriod(timeStart1, timeEnd1, timeNow)
if result1 == True:
    result1 = str('**Terbuka** ✅')
else:
    result1 = str('**Tertutup** :no_entry:')

#Jadwal Kedua
timeStart2 = '16:00'
timeEnd2 = '20:00'
result2 = isNowInTimePeriod(timeStart2, timeEnd2, timeNow)
if result2 == True:
    result2 = str('**Terbuka** ✅')
else:
    result2 = str('**Tertutup** :no_entry:')

#Jadwal Ketiga
timeStart3 = '00:00'
timeEnd3 = '04:00'
result3 = isNowInTimePeriod(timeStart3, timeEnd3, timeNow)
if result3 == True:
    result3 = str('**Terbuka** ✅')
else:
    result3 = str('**Tertutup** :no_entry:')