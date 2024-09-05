import re
import math

def TinhSoNut(n):
    total = 0
    while (n > 0):
        total = total + n % 10
        n = int(n / 10)
    return int(total)

def ChangeMinuteToHour(minute):
    hour = 0
    DayNight='AM'
    hour = int(minute / 60)
    minute = minute - (60 * hour)
    
    while (hour > 12):
        hour = hour - 12
        if DayNight == 'AM':
            DayNight='PM'
        else :
            DayNight = 'AM'
    
    Time = 'Thoi gian hien tai la : ' + str(hour)+':'+str(minute)+str(DayNight)

    return Time




#global enviroment
print('Bai 1')
BangSoXe = input('Vui long nhap bang so xe cua ban: ')
BangSoXeSlide = BangSoXe[6:]
BangSoXeSplit = BangSoXeSlide.split('.')
Num = BangSoXeSplit[-1]
Num2 = BangSoXeSplit[0]
TongSo = TinhSoNut(int(Num)) +TinhSoNut(int(Num2))
print('Tong so nut cua bien so xe nay la: ' + str(TongSo)) 

print('Bai 2')
SoPhut = int(input('So phut da troi ke tu nua dem(0:00AM): '))
print(ChangeMinuteToHour(SoPhut)) 

print('Bai 3')
MaxKm = float(input('Nhap so km toi da xe co the di: '))
Cunsumption = float(input('Nhap so luong nhien lieu tieu thu(l/100km): '))
Distance = float(input('Nhap quang duong ban muon di(km): '))
Price = int(input('Nhap so tien 1 lit xang: '))


SoNgay = math.ceil((Distance/MaxKm))

TotalPrice =  float((Distance/100)*Cunsumption*Price)

print('So ngay can de di het '+ str(Distance) + 'km la: '+str(SoNgay)) 
print('So tien can tra de di duoc '+ str(Distance) + 'km la: '+str(TotalPrice))








