import math

def TongSoDau(TongSoNguoi):
    TongSoDau = 0
    for i in range (1,TongSoNguoi+1,1):
        SoDau = int(input('Nhap so dau cua nguoi thu {}: '.format(i)))
        TongSoDau += SoDau
    print('Tong so dau moi nguoi thu duoc la: '+str(TongSoDau))    
    return int(TongSoDau)    

def XuLyTien(TongSoTien):
    SoTo_500000 = 0
    SoTo_200000= 0
    SoTo_100000 = 0
    SoTo_50000 = 0
    SoTo_20000 = 0
    SoTo_10000 = 0
    SoTo_5000 = 0
    SoTo_2000 = 0
    SoTo_1000 = 0
    SoTo_500 = 0
    SoTo_200 = 0
    
    print('De tra so tien: '+str(TongSoTien)+'vnd khach hang can:')
    while TongSoTien >= 500000:
        TongSoTien -= 500000
        SoTo_500000 += 1
    while TongSoTien >= 200000:
        TongSoTien -= 200000
        SoTo_200000 += 1
    while TongSoTien >= 100000:
        TongSoTien -= 100000
        SoTo_100000 += 1
    while TongSoTien >= 50000:
        TongSoTien -= 50000
        SoTo_50000 += 1
    while TongSoTien >= 20000:
        TongSoTien -= 20000
        SoTo_20000 += 1
    while TongSoTien >= 10000:
        TongSoTien -= 10000
        SoTo_10000 += 1
    while TongSoTien >= 5000:
        TongSoTien -= 5000
        SoTo_5000 += 1
    while TongSoTien >= 2000:
        TongSoTien -= 2000
        SoTo_2000 += 1
    while TongSoTien >= 1000:
        TongSoTien -= 1000
        SoTo_1000 += 1
    while TongSoTien >= 500:
        TongSoTien -= 500
        SoTo_500 += 1
    while TongSoTien >= 200:
        TongSoTien -= 200
        SoTo_200 += 1
    ConLai = TongSoTien


    print('- ' +str(SoTo_500000) + ' to 500000')
    print('- ' +str(SoTo_200000) + ' to 200000')
    print('- ' +str(SoTo_100000) + ' to 100000')
    print('- ' +str(SoTo_50000) + ' to 50000')
    print('- ' +str(SoTo_20000) + ' to 20000')
    print('- ' +str(SoTo_10000) + ' to 10000')
    print('- ' +str(SoTo_5000) + ' to 5000')
    print('- ' +str(SoTo_2000) + ' to 2000')
    print('- ' +str(SoTo_1000) + ' to 1000')
    print('- ' +str(SoTo_500) + ' to 500')
    print('- ' +str(SoTo_200) + ' to 200')
    print('- Con du ' +str(ConLai) )
    
    







""" #Global Environment
print('Bai 1:')
print('Vuon Dau Da Lat')
TongSoNguoi = int(input('Nhap so nguoi tham gia chuong trinh: '))
TongSo_Dau =TongSoDau(TongSoNguoi)
SoDauNhanDuoc =math.floor(TongSo_Dau / TongSoNguoi)*TongSoNguoi 
print('So dau nhom nguoi nay nhan duoc la: '+str(SoDauNhanDuoc))
SoDauTraLai = TongSo_Dau - SoDauNhanDuoc
print('So dau trai lai la: '+str(SoDauTraLai))


print('Bai 2:')
TongSoTien = int(input('Nhap tong so tien khach hang mang theo: '))
XuLyTien(TongSoTien)  """

print('Bai 3')
TongSoTienPhaiTra = int(input('Nhap tong so tien khach hang phai tra: '))
ListMenhGia = [200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000]
ListToTien=[]
TongTienMangTheo = 0
for i in ListMenhGia:
    TongToTien= 0
    TongToTien = int(input('Vui Long Nhap So To Tien Menh Gia {}vnd: '.format(i)))
    ListToTien.append(TongToTien)
    TongTienMangTheo += i*TongToTien

ListToTien.reverse()
ListMenhGia.reverse()
TongTienConLai = TongTienMangTheo
TongTienDaTra = 0
a=0

print('Tong tien khach hang mang theo la: '+str(TongTienMangTheo))
if TongTienMangTheo >TongSoTienPhaiTra:
    print('Thanh toan thanh cong!!')
    for i in ListToTien:
        
        if TongTienConLai >= ListMenhGia[a]:
            TongTienDaTra += i * ListMenhGia[a]
            TongTienConLai -= i  * ListMenhGia[a]   
            print('So to co menh gia {} khach nay can tra la {}'.format(ListMenhGia[a],i))
            a+=1
            if a > 10:
                break
            if TongTienDaTra >= TongSoTienPhaiTra:
                break
        if TongTienDaTra >= TongSoTienPhaiTra:
            break
    print('So tien thoi lai cho khach hang la: '+str(TongTienDaTra-TongSoTienPhaiTra))
else:
    print('ERROR: Khong du tien')



        



