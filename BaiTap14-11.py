from sre_constants import BRANCH

def CheckPerfectNumber(n):
    sum = 0
    for i in range(1, n):
        if (n % i) == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False

def tinh(sohang):
    f = 1
    while (sohang > 1):
        f = f * sohang
        sohang = sohang - 1
    return f
 
def Variable(n, r):
    return int(tinh(n) / (tinh(n - r) * tinh(r)))

class PhanSo():
    def __init__(self,paraTu,paraMau):
        self.tuso = paraTu
        self.mauso = paraMau
    def In(tuso, mauso):
        return '{}/{}'.format(tuso,mauso)
    def ucln(tuso,mauso):
        temp1 = tuso
        temp2 = mauso
        while (temp1 != temp2):
            if (temp1 > temp2):
                temp1 -= temp2;
            else:
                if(temp1<0):
                    temp1 +=temp2
                else:   
                    temp2 -= temp1;
        uscln = temp1;
        
        return uscln
    def rutgontu(ucln,tuso):
        tusosaukhirut = int(tuso / ucln)
        return tusosaukhirut
    def rutgonmau(ucln,mauso):
        mausosaukhirut = int(mauso / ucln)
        return mausosaukhirut

    def CongPhanSo(tuso1, mauso1,tuso2, mauso2):
        listpphanso = []
        congtuso = (tuso1*mauso2) + (tuso2*mauso1)
        listpphanso.append(congtuso)
        congmauso = mauso1 * mauso2
        listpphanso.append(congmauso)

        return listpphanso
    def TruPhanSo(tuso1, mauso1,tuso2, mauso2):
        listpphanso = []
        trutuso = (tuso1*mauso2) - (tuso2*mauso1)
        listpphanso.append(trutuso)
        trumauso = mauso1 * mauso2
        listpphanso.append(trumauso)
        return listpphanso
    def TichPhanSo(tuso1, mauso1,tuso2, mauso2):
        listphanso = []
        nhantuso = tuso1 * tuso2
        nhanmauso = mauso1 * mauso2
        listphanso.append(nhantuso)
        listphanso.append( nhanmauso)
        return listphanso
    def ThuongPhanSo(tuso1, mauso1,tuso2, mauso2):
        listphanso = []
        chiatuso =  tuso1 * mauso2 
        chiamauso = tuso2 * mauso1
        listphanso.append(chiatuso)
        listphanso.append( chiamauso)
        return listphanso

#Global Environment

print('Bai 1')
Num_A = int(input('Nhap so A: '))
Num_B = int(input('Nhap so B: '))
List_PerfectNumber = []
for i in range(Num_A, Num_B+1):
    if CheckPerfectNumber(i):
        List_PerfectNumber.append(i)
    i += 1
print(List_PerfectNumber)


print('Bai 2')
while True:
    sohang = int(input("Hãy nhập số hàng: "))
    if sohang<0:
        print("Không nhận giá trị âm, nhập lại")
    else:
        break
print("\nTam giác Pascal là: ")
for i in range(0, sohang + 1):
    for j in range(0, sohang - i + 1):
        print("", end = "")
 
    for j in range(0, i + 1):
        print(" {:<3}".format(Variable(i, j)), end="")
 
    print("")


print('Bai 3')
tu1 = int(input("Hãy nhập tử số của phân số 1: "))
mau1 = int(input("Hãy nhập mẫu số của phân số 1: "))

phanso1 = PhanSo(tu1, mau1)
print("Phân số sau khi nhập là: ")
print(PhanSo.In(tu1, mau1))
ucln = PhanSo.ucln(tu1, mau1)
Tuso1 = tu1
Mauso1 =mau1
if ucln ==1:
    print("Phân số này đã tối giản\n")
else:
    Tuso1 = PhanSo.rutgontu(ucln,tu1)
    Mauso1 = PhanSo.rutgonmau(ucln,mau1)
    print("Phân số sau khi tối giản là: ")
    print('{}/{}'.format(Tuso1, Mauso1))

tu2 = int(input("Hãy nhập tử số của phân số 2: "))
mau2 = int(input("Hãy nhập mẫu số của phân số 2: "))
phanso2 = PhanSo(tu2, mau2)
print("Phân số sau khi nhập là: ")
print(PhanSo.In(tu2, mau2))
ucln1 = PhanSo.ucln(tu2, mau2)
Tuso2 = tu2
Mauso2=mau2
if ucln1 ==1:
    print("Phân số này đã tối giản\n")
else:
    Tuso2 = PhanSo.rutgontu(ucln1,tu2)
    Mauso2 = PhanSo.rutgonmau(ucln1,mau2)
    print("Phân số sau khi tối giản là: ")
    print('{}/{}'.format(Tuso2, Mauso2))

while True:
    print("---------------------")

    print("1: Cộng hai phân số")
    print("2: Trừ hai phân số")
    print("3: Nhân hai phân số")
    print("4: Chia hai phân số")
    print("0: Thoát")
    print("---------------------\n")


    Choose =  int(input("Hãy chọn chức năng mà bạn muốn tính: "))
    tinhphanso = []
    
    if Choose ==1:
        print("\n---------------------")
        print("Cộng Phân Số")
       
        tinhphanso =PhanSo.CongPhanSo(Tuso1,Mauso1,Tuso2, Mauso2)
        tucong = tinhphanso[0]
        maucong = tinhphanso[1]

        print('{}/{} + {}/{} = {}/{}'.format(Tuso1,Mauso1,Tuso2,Mauso2,tucong, maucong))

        ucln1 = PhanSo.ucln(tucong,maucong)
        if ucln1 ==1:
            print("Phân số này đã tối giản")
        else: 
            Tusorutgon = PhanSo.rutgontu(ucln1,tucong)

            Mausorutgon = PhanSo.rutgonmau(ucln1,maucong)

            print("{}/{} sau khi rút gọn là: {}/{}".format(tucong,maucong, Tusorutgon,Mausorutgon))

            
    elif Choose ==2:
        print("\n---------------------")
        print("Trừ Phân Số")
        tinhphanso.clear()
        tinhphanso =PhanSo.TruPhanSo(Tuso1,Mauso1,Tuso2, Mauso2)
        tutru = tinhphanso[0]
        mautru = tinhphanso[1]

        print('{}/{} - {}/{} = {}/{}'.format(Tuso1,Mauso1,Tuso2,Mauso2,tutru, mautru))

        ucln1 = PhanSo.ucln(tutru,mautru)
        if ucln1 ==1  :
            print("Phân số này đã tối giản")
        else: 
            Tusorutgon = PhanSo.rutgontu(ucln1,tutru)

            Mausorutgon = PhanSo.rutgonmau(ucln1,mautru)

            print("{}/{} sau khi rút gọn là: {}/{}".format(tutru,mautru, Tusorutgon,Mausorutgon))

    elif Choose ==3:
        print("\n---------------------")
        print("Nhân Phân Số")
        tinhphanso.clear()
        tinhphanso =PhanSo.TichPhanSo(Tuso1,Mauso1,Tuso2, Mauso2)
        tunhan = tinhphanso[0]
        maunhan = tinhphanso[1]

        print('{}/{} x {}/{} = {}/{}'.format(Tuso1,Mauso1,Tuso2,Mauso2,tunhan, maunhan))

        ucln1 = PhanSo.ucln(tunhan,maunhan)
        if ucln1 ==1:
            print("Phân số này đã tối giản")
        else: 

            Tusorutgon = PhanSo.rutgontu(ucln1,tunhan)

            Mausorutgon = PhanSo.rutgonmau(ucln1,maunhan)

            print("{}/{} sau khi rút gọn là: {}/{}".format(tunhan,maunhan, Tusorutgon,Mausorutgon))
            
    elif Choose ==4:
        print("---------------------")
        print("Chia Phân Số")
        tinhphanso.clear()
        tinhphanso =PhanSo.ThuongPhanSo(Tuso1,Mauso1,Tuso2, Mauso2)
        tuchia = tinhphanso[0]
        mauchia = tinhphanso[1]

        print('{}/{} / {}/{} = {}/{}'.format(Tuso1,Mauso1,Tuso2,Mauso2,tuchia, mauchia))

        ucln1 = PhanSo.ucln(tuchia,mauchia)
        if ucln1 ==1:
            print("Phân số này đã tối giản")
        else: 
            Tusorutgon = PhanSo.rutgontu(ucln1,tuchia)

            Mausorutgon = PhanSo.rutgonmau(ucln1,mauchia)

            print("{}/{} sau khi rút gọn là: {}/{}".format(tuchia,mauchia, Tusorutgon,Mausorutgon))
    else:
        break