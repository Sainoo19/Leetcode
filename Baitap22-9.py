import math
Listnum= [ ]
def AddList(Listnum):
    while True:
        num=int(input('Nhap 1 so vao mang (nhap -1 de ket thuc nhap): '))
   
        if num == -1:
            break
        Listnum.append(num)
    


def CheckSoNguyenTo(n):
    if(n<2):
        return False
    i=2;
    while i <= n/2:
        if(n%i == 0):
            return False
        i+=1
    return True



def SumSoNguyenTo_List(Listnum):
    sum = 0
    count = 0
    
    for a in Listnum:
        if CheckSoNguyenTo(a) == True:
            sum += a
    return sum

def MaxList(Listnum): 
    Listnum.sort()
    return Listnum[-1]

def MinList(Listnum):
    Listnum.sort()
    return Listnum[0]


AddList(Listnum)
print('List numbers: ',Listnum)

print('List prime numbers: ')
for i in Listnum:
    if(CheckSoNguyenTo(i)):
        print(i, end= " ")

Sum = SumSoNguyenTo_List(Listnum)
print('Tong cac so nguyen to: ',Sum)
print('Max list: ',str(MaxList(Listnum)),'|| Min list: ',str(MinList(Listnum)))
    
    

    