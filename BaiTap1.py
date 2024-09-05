import math
print("BAI 1/")
#input
hoten=input("Nhap ho ten sinh vien: ")
ho= hoten.split()[0]
ten= hoten.split()[-1]
mssv = input("Nhap ma so sinh vien :")

#output
print("Ho ten sinh vien:",hoten)

print("Email sinh vien :" ,ten.lower() + "." + mssv+"@vanlanguni.vn")

print("BAI 2/")
print ("Tất cả các số nguyên tố nhỏ hơn 100 là: ");
bool01 = 0
sb = "";
sb = sb + "2 3" + " ";

for i in range (101):
    if (i < 2):
        bool01 = 0 
    squareRoot = int(math.sqrt(i));
    for a in range(2, squareRoot + 1):
        if (i % a == 0):
            bool01 = 0
            break
        else:
            bool01 = 1
    if bool01 == 1:
        sb += str(i) + " ";
    i = i + 2;
print(sb);