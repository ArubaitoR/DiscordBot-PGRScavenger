# PGR COOP
# 08:00am - 12:00 pm
# 04:00pm - 08:00pm
# 12:00am - 04:00am
import os, time

os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()

def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else:
        return nowTime >= startTime or nowTime <= endTime


#Jam Sekarang
timeNow = time.strftime("%H:%M", time.localtime())
print('Jam Saat Ini:', timeNow)

#Jadwal Pertama
timeStart = '08:00'
timeEnd = '12:00'
print(f'Jadwal Pertama {timeStart} - {timeEnd}:', isNowInTimePeriod(timeStart, timeEnd, timeNow))

#Jadwal Kedua
timeStart = '16:00'
timeEnd = '20:00'
print(f'Jadwal Pertama {timeStart} - {timeEnd}:', isNowInTimePeriod(timeStart, timeEnd, timeNow))

#Jadwal Ketiga
timeStart = '00:00'
timeEnd = '04:00'
print(f'Jadwal Pertama {timeStart} - {timeEnd}:', isNowInTimePeriod(timeStart, timeEnd, timeNow))