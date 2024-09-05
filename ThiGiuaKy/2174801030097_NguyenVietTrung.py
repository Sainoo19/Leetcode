import string


def readFile(l, filename):
    try:     
        f = open(f"{filename}", "r", encoding="utf-8")
        
        content = f.read()
        f.close()

        messageList = content.split("\n")
        for i in range(len(messageList)):
            l.append(messageList[i])
        print(f"Nhan du lieu tu {filename} thanh cong")
    except FileNotFoundError:
        print(f"Khong tim thay file {filename} ")
        
    

def encrypt(s):
    stringValue = s.lower()
    result = ""
    for i in range(len(stringValue)):
        for j in range(len(char)):
            if stringValue[i] == char[j]:
               result += f"{number[j]},"
            elif stringValue[i] == ' ':
                result += ' ,'
                break
    return result



def decrypt(s):
    stringValue = s.lower()
    result = ""
    for i in range(len(stringValue)):
        for j in range(len(number)):
            if stringValue[i] == number[j]:
               result += f"{char[j]},"
            elif stringValue[i] == ' ':
                result += ' ,'
                break
    return result


def writeFile(l):
    List = []
    f = open("output.txt", "w", encoding="utf-8") 
    f.writelines(List)
    f.close()
    print("Xuat ra file output.txt thanh cong")
    

#Global EV
char_ascii = string.ascii_lowercase
char = []
for i in char_ascii:
    char.append(i)
number = []
for i in range(3, 27):
    number.append(i)
for i in range(1, 3):
    number.append(i)

listOfSentences = []
Dict_MaHoa = {"key": [], "value": []}


File_name = input("Nhap ten file ban muon ma hoa: ")
readFile(listOfSentences, File_name)


for i in range(len(listOfSentences)):
    Dict_MaHoa["key"].append(listOfSentences[i])
    r = encrypt(listOfSentences[i])
    Dict_MaHoa["value"].append(r)
print(Dict_MaHoa)