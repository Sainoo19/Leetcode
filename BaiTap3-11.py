import math
import Const
def AddDict(Dict):
        Dict.clear()
        Column = input("Enter column[A-H]: ")
        row = int(input("Enter row[1-8]: "))
      
        Dict[Column] = row



def MuaVang(sotien, gialuong, giachi):
    soluongvang = int(sotien/gialuong)
    sotienconlai = sotien%gialuong
    
    sochi= int(sotienconlai/giachi)
    sotiencuoicung = sotienconlai%giachi
    print('Với {}vnd, bạn có thể mua được {} lượng '.format(sotien, soluongvang))
    if sochi>0:
        print("{} chỉ vàng".format(sochi))
    if sotiencuoicung>0:
        print('Và còn dư {}vnd'.format(sotiencuoicung))

print('Bai 1')
while True:
    sotien = int(input("Hãy nhập số tiền đang có: "))
    if(sotien<0 ):
        print("Không nhận số âm, nhập lại")
    else:
        break
while True:
    gia1luong = int(input("Hãy nhập số tiền một lượng: "))

    if(gia1luong<0 ):
        print("Không nhận số âm, nhập lại")
    else:
        break
while True:
    gia1chi = int(input("Hãy nhập số tiền một chỉ: "))

    if(gia1chi<0 ):
        print("Không nhận số âm, nhập lại")
    else:
        break


MuaVang(sotien,gia1luong,gia1chi)

print('Bai 2')
SoGio = int(input('Vui Long Nhap So Gio: '))

SoPhut = int(input('Vui Long Nhap So Phut: '))
#thầy kêu khỏi tính trường hợp kim giờ di chuyển do số phút nhưng em muón tự thử thách nên em làm thử
#Ta thấy để kim giờ nhích lên 1 số cần 60 phút nói cách khác kim giờ đồng thời di chuyển cùng kim phút và khi kim phut chạy được 60 phút thì kim giờ nhích lên 1 giờ
#Vậy thì quãng đường di chuyển của kim giờ bằng số giờ hiện tại + số phút chia 60 
#vd 4h20p ta lấy 20/60  dc 1/3 ta lấy 4h + 1/3 vậy là ra quãng đường kim giờ đã di chuyển
SoGioChange = SoGio + SoPhut/60
SoGioCuaPhut = SoPhut/5
SoChenhLech = abs(SoGioChange - SoGioCuaPhut)
Angle = SoChenhLech * Const.rad_hour
if Angle > 180:
    Angle = 360 - Angle
print('Goc tao boi kim gio tai thoi diem '+str(SoGio)+' va kim phut tai thoi diem '+str(SoPhut)+' la: '+ str(Angle)) 

print('Bai 3')
XuatPhat = {}
DiemDen = {}
AddDict(XuatPhat)
AddDict(DiemDen)
for i in XuatPhat.values():
    VL_XuatPhat = i
for i in DiemDen.values():
    VL_DiemDen = i
while XuatPhat.keys() == DiemDen.keys() and VL_XuatPhat == VL_DiemDen :
    print('Quan co chua di chuyen vui long chon lai diem den cho quan co')
    AddDict(DiemDen)
    for i in DiemDen.values():
        VL_DiemDen = i
        
if XuatPhat.keys() == DiemDen.keys() or VL_XuatPhat == VL_DiemDen :
    print('Quan xe nay co the di chuyen tu vi tri '+str(XuatPhat)+' den vi tri '+str(DiemDen)+' trong 1 nuoc di')
else:
    print('Khong the di chuyen quan xe den vi tri '+str(DiemDen)+' trong 1 nuoc di')


