import string
import re
import math

def nhaptheki():
    try:
        tki = int(input('Nhập vào thế kỉ: '))
        if tki < 1 or tki > 99:
            return nhaptheki()
    except:
        print('Lỗi! Tối đa là thế kỉ 99')
        return nhaptheki()
    return tki

def AddDict(Dict):
        Dict.clear()
        Column = input("Enter column[A-H]: ")
        row = int(input("Enter row[1-8]: "))
        Dict[Column] = row

def isPrimeNum(n):
    if n < 2:
        return False
    if n == 2:
        return True
    tg = int(math.sqrt(n))
    for i in range(2, tg + 1):
        if (n % i) == 0:
            return False
    return True

class Converter(object):
    def toCelcius(self, fahrenheit):
        s = (fahrenheit - 32) / 1.8
        return "%.2f" % s + " C"
    def toFahrenheit(self, celcius):
        s = (celcius * 1.) + 32
        return "%.2f" % s + " F"
    def toCentimeter(self, inches):
        s = (inches * 2.54)
        return "%.2f" % s + " cm"
    def toInches(self, centimeter):
        s = (centimeter / 2.54)
        return "%.2f" % s + " Inches"


#Global environment
print('Cau 1')           
Diem1 = {}
Diem2 = {}
AddDict(Diem1)
AddDict(Diem2)



char_ascii = string.ascii_lowercase
Column = char_ascii[:8]
for i in Diem1.keys():
    Column_Diem1 = i
for i in Diem2.keys():
    Column_Diem2 = i
for i in Diem1.values():
    Row_Diem1 = i
for i in Diem2.values():
    Row_Diem2 = i


if (int(Column.rfind(Column_Diem1))%2 == 0 and int(Row_Diem1)%2 == 0) or (int(Column.rfind(Column_Diem1))%2 != 0 and int(Row_Diem1)%2 != 0):
    ChessBox_Color1 = "White"
if (int(Column.rfind(Column_Diem2))%2 == 0 and int(Row_Diem2)%2 == 0) or (int(Column.rfind(Column_Diem2))%2 != 0 and int(Row_Diem2)%2 != 0):
    ChessBox_Color2 = "White"


if (int(Column.rfind(Column_Diem1))%2 != 0 and int(Row_Diem1)%2 == 0) or (int(Column.rfind(Column_Diem1))%2 == 0 and int(Row_Diem1)%2 != 0):
    ChessBox_Color1 = "Black"
if (int(Column.rfind(Column_Diem2))%2 != 0 and int(Row_Diem2)%2 == 0) or (int(Column.rfind(Column_Diem2))%2 == 0 and int(Row_Diem2)%2 != 0):
    ChessBox_Color2 = "Black"

print('Mau cua o 1 la: ',ChessBox_Color1)
print('Mau cua o 2 la: ',ChessBox_Color2)
if ChessBox_Color1==ChessBox_Color2:
    print('Hai o nay cung mau!!')
else:
    print('Hai o nay khac mau!!')


print('Cau 2')   
theki = nhaptheki()

bdtk = (theki - 1) * 100 + 1

kttk = (theki ) * 100

lstnamnhuan = []
for j in range(bdtk,kttk + 1,1):
    if(j % 4 == 0 and j % 100 != 0) or j % 400 == 0:
        
        lstnamnhuan.append(j)
print(lstnamnhuan)


print('\nCau 3')
check = True
while check:
    a = int(input('Nhập a: '))
    b = int(input('Nhập b: '))
    if a < b:
        check = False

listPrimeNum = []
for i in range(a, b+1):
    if isPrimeNum(i):
        listPrimeNum.append(i)
    i = i + 2
print(listPrimeNum)

print('\nCau 4')   
a1 = Converter()
print(a1.toCelcius(50))
print(a1.toFahrenheit(50))
print(a1.toCentimeter(50))
print(a1.toInches(50))
