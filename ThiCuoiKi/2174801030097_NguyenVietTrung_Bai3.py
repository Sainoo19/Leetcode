import sys
class myNumber(object):
    def __init__(self, n):
        self.n = n

    def readFile(filename):
        """
        It opens a file, reads the contents, closes the file, and returns the contents
        
        :param filename: The name of the file you want to read
        :return: The content of the file
        """

        try:
            f = open(f"{filename}.txt", "r", encoding="utf-8")
            
            content = f.read()
            f.close()

            print(f"Nhan du lieu tu {filename} thanh cong")
            return content
        except FileNotFoundError:
            print(f"Khong tim thay file {filename} ")
            print('Vui long kiem tra lai ten file va khong can nhap dinh dang file')
            sys.exit()

    def Factorial(x):
        """
        The function takes a number, and if it's 1, it returns 1. Otherwise, it returns the number
        multiplied by the factorial of the number minus 1
        
        :param x: The number you want to find the factorial of
        :return: The factorial of the number.
        """

        if x == 1:
            return x

        return x * myNumber.Factorial(x-1)

    def testPrim(x):
        """
        > The function `testPrim` takes a number `x` and returns `True` if `x` is prime, and `False`
        otherwise
        
        :param x: the number to be tested
        :return: the boolean value of isprime.
        """

        isprime = True
        if x < 1:
            isprime = False
            return isprime

        for i in range(2, x):
            if x % i == 0:
                isprime = False 
                break

        return isprime

    def testCoPrims(x, y):
        """
        If x and y are prime numbers and the greatest common divisor of x and y is 1, then x and y are
        coprime
        
        :param x: the first number
        :param y: the number to be tested
        :return: True or False
        """
        if myNumber.testPrim(x) == True and myNumber.testPrim(x) == myNumber.testPrim(y):
            if uscln(x,y) == 1:
                return True
            else:
                return False
        else:
            return False

    def tableMul(x):
        """
        It takes a number as input and returns a list of numbers that are the multiplication table of the
        input number
        
        :param x: The number whose multiplication table is to be calculated
        :return: A list of the multiplication table of the number x.
        """
        List = []
        for i in range(1, 11):
            List.append(i*x)
        return List

    def divPrim(x):
        """
        It takes a number and returns a list of all the numbers that divide into it
        
        :param x: The number you want to find the prime factors of
        :return: A list of all the divisors of the number x.
        """
        List = []
        for i in range(1, x+1):
            if (x % i == 0):
                List.append(i)
        return List


def uscln(a, b):
    """
    If b is 0, return a. Otherwise, return the result of calling uscln with b and a mod b
    
    :param a: the first number
    :param b: the number of the first number
    :return: The greatest common divisor of a and b.
    """

    if (b == 0):
        return a
    return uscln(b, a % b)

def writeFile(filename, text):
    """
    It opens a file, writes text to it, and then closes the file
    
    :param filename: The name of the file you want to write to
    :param text: The text to be written to the file
    """

    f = open(f"{filename}.txt", "a", encoding="utf-8")
    f.write(text)
    f.close()


#Global Environment
String_Output = ""
number = myNumber(3)
List_Input=[]
FileName_Input = input('Nhap ten file muon su dung(khong can nhap dinh dang file .txt): ')
List_Input = myNumber.readFile(FileName_Input).split()

x = int(List_Input[0])
y=  int(List_Input[1])
FileName_Output = input('Nhap ten file muon xuat du lieu: ')

String_Output += f"\nFactorial({number.n}) = {myNumber.Factorial(number.n)}\n"
String_Output += f"testPrim({x}) = {myNumber.testPrim(x)}\n"
String_Output += f"testCoPrims({x}, {y}) = {myNumber.testCoPrims(x, y)}\n"
String_Output += f"tableMul({number.n}) = {myNumber.tableMul(number.n)}\n"
String_Output += f"divPrim({number.n}) = {myNumber.divPrim(number.n)}"
writeFile(FileName_Output, String_Output)
