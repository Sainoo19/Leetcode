import math

def AddDict_ChinaChess(Dict):
        Dict.clear()
        Column = int(input("Enter column[4-6]: "))
        row = int(input("Enter row[1-3]: "))
        Dict[Column] = row

def AddDict_Chocolate(Dict):
        Dict.clear()
        Column = int(input("Enter column: "))
        row = int(input("Enter row: "))
        Dict[Column] = row


def find_square_number(n):
    flag = 0
    if any(i**2 == n for i in range(n+1)):
        flag = 1
    return flag



Diem1 = {}
Diem2 = {}
Chocolate_Info= {}

print('Bai 1')
print('Nhap vi tri bat dau cua quan tuong')
AddDict_ChinaChess(Diem1)
print('Nhap vi tri can di den cua quan tuong')
AddDict_ChinaChess(Diem2)

for i in Diem1.keys():
    Column_Diem1 = i
for i in Diem2.keys():
    Column_Diem2 = i
for i in Diem1.values():
    Row_Diem1 = i
for i in Diem2.values():
    Row_Diem2 = i

SoNuocDaDi = 0
while True:
    if Column_Diem1 > Column_Diem2:
        Column_Diem1 = Column_Diem1 - 1
        SoNuocDaDi += 1
    else: break
while True:
    if Column_Diem1 < Column_Diem2:
        Column_Diem1 = Column_Diem1 + 1
        SoNuocDaDi += 1
    else: break
while True:
    if Row_Diem1 > Row_Diem2:
        Row_Diem1 = Row_Diem1 - 1
        SoNuocDaDi += 1
    else: break
while True:
    if Row_Diem1 < Row_Diem2:
        Row_Diem1 = Row_Diem1 + 1
        SoNuocDaDi += 1
    else: break

print('Quan tuong can {} nuoc di de di tu {} den {}'.format(SoNuocDaDi,Diem1,Diem2))

print('Bai 2')
print('Nhap thong so cua thanh Chocolate')
AddDict_Chocolate(Chocolate_Info)

while True:
    Chocolate_Box = int(input('Nhap so o vuong muon be ra:'))
    if math.sqrt(Chocolate_Box) % 1 != 0:
        print('So o vuong muon be ra phai tao thanh 1 hinh vuong')
    else:
        break
Canh_ChocolateBox = int(math.sqrt(Chocolate_Box))
for i in Chocolate_Info.keys():
    Column_Chocolate_Info = i
for i in Chocolate_Info.values():
    Row_Chocolate_Info = i
print('De be thanh chocolate thanh hinh vuong co {} o vuong nho'.format(Chocolate_Box))
print('Buoc 1')
Column = Column_Chocolate_Info - Canh_ChocolateBox
print('Be thanh chocolate {} cot'.format(Column))
print('Buoc 2')
Row = Row_Chocolate_Info - Canh_ChocolateBox
print('Be thanh chocolate {} dong'.format(Row))

print('Bai 3')
Num_A = int(input('Nhap so A: '))
Num_B = int(input('Nhap so B: '))
List_SquareNumber = []
for i in range(Num_A, Num_B+1):
    if find_square_number(i) == 1:
        List_SquareNumber.append(i)
    i += 1
print(List_SquareNumber)

