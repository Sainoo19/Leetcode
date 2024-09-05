
def FindNumber(L,x):
    if x in L:
        vitri =  L.index(x)
        return vitri
    else:
        #a.	Viết hàm findNumber(x) tìm vị trí của x trong L,
        # nếu không tìm thấy trả về None
        return None
def findNextSameSign(L,x):
    vỉtri = 0
    if FindNumber(L,x) == None:
        print("Không tồn tại giá trị {} trong list".format(x))
    else:
        vitri = FindNumber(L,x)
        while True:
            vitri +=1
            y = L[vitri]
            if y== 0:
                print("Số 0 không phải là số nguyên âm lẫn nguyên dương, chuyển đến số tiếp theo")
            if (x> 0 and y>0) or (x<0 and y<0):
                return y
        

    
L = [3,5,-4,7,-9,2,0,-11,3,7,4,0,4,3,3,5]
print("Dãy số nhập vào là: ")
print(L)
sox = int(input("\nHãy nhập số cần tìm: "))
tim = FindNumber(L,sox)
print("Số {} nằm ở vị trí {}".format(sox,tim))
soliensau = int(input("\nHãy nhập số để tim số cùng dấu liền sau nó trong dãy số: "))
inso = findNextSameSign(L,soliensau)
print("Số liền sau {} và có cùng dấu với {} là {}".format(soliensau, soliensau, inso))
