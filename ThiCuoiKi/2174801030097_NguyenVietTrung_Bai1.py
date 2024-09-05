import sys
def readFile(filename):
    """
    It reads a file and returns a list of strings
    
    :param filename: The name of the file to read
    :return: A list of strings
    """
    listString = []
    try:     
        f = open(f"{filename}.txt", "r", encoding="utf-8")
        
        content = f.read()
        f.close()

        messageList = content.split("\n")
        for i in range(len(messageList)):
            listString.append(messageList[i])
        print(f"Nhan du lieu tu {filename} thanh cong")
        return listString
    except FileNotFoundError:
        print(f"Khong tim thay file {filename} ")
        print('Vui long kiem tra lai ten file va khong can nhap dinh dang file')
        sys.exit()
    

def bumpString(List,text):
    """
    The function takes a list and a string as input, and returns a list of strings
    
    :param List: The list that you want to add the text to
    :param text: The string that you want to bump
    :return: The list is being returned.
    """

    textOutPut = " "
    for i in range(0,len(text),1):
        textOutPut += text[i]
        List.append(textOutPut)

    return List
        
def writeFile(textOutput,filename):
    """
    This function takes a list of strings and writes them to a file
    
    :param textOutput: The text that you want to write to the file
    :param filename: The name of the file you want to write to
    """
    f = open(f"{filename}.txt", "w", encoding="utf-8") 
    f.writelines(textOutput)
    f.close()
    
#Global Environment       
myStrings = []
myBumpString = []
fileName_Input = input('Nhap ten file muon su dung(khong can nhap dinh dang file .txt): ')
myStrings = readFile(fileName_Input)
fileName_Output = input('Nhap ten file muon xuat ket qua: ')
StringOutput = ""

for i in range(0,len(myStrings),1):
    myBumpString.clear()
    text = myStrings[i]
    bumpString(myBumpString,text)
    for a in range(0,len(myBumpString),1):
        StringOutput += myBumpString[a] + " "
        writeFile(StringOutput,fileName_Output) 
    StringOutput += "\n"
    
    





