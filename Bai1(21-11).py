def Dem(L):
    ListSo = {}
    
    for i in L:
        solan =0
        for u in L:
            if i == u:
                solan +=1
        ListSo[i] = solan
    return ListSo

def SapXepGiamDan(listso):
    values_sorted = sorted(listso.items(),reverse=True, key = lambda x : x[1])
    return values_sorted

print("\nDanh sách ban đầu là: ")
L = [3,5,-4,7,-9,2,0,-11,3,7,4,0,4,3,3,5,7,2,-4,6,74]
print(L)
listso ={}
listso = Dem(L)
print("\nĐếm số lần xuất hiện của các phần tử: ")
print(listso)
print("\nDanh sách sau khi sắp xếp giảm dần theo thứ tự xuất hiện là: ")
print(SapXepGiamDan(listso))
