def CheckPerfectNumber(n):
    sum = 0
    for i in range(1, n):
        if (n % i) == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False

while True:
        num = int(input('Nhap vao so nguyen bat ky lon hon 0: '))
        if CheckPerfectNumber(num):
            print(num, ' la so hoan hao')
            break
        else:
            print(num, ' khong la so hoan hao')