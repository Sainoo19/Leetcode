import sys

MorseCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '&': '.-...', "'": '.----.',
    '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--',
    '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.',
    '"': '.-..-.', '?': '..--..', '/': '-..-.'
             } 

def readFile(filename):
    """
    It opens a file, reads the contents, splits the contents into a list, and appends the list to a
    global variable
    
    :param filename: The name of the file to read
    """


    try:
        f = open(f"{filename}.txt", "r", encoding="utf-8")
        content = f.read()
        f.close()
        List = content.split("\n")
        
        for i in List:
            inputData.append(i)
        print(f"Nhan du lieu tu {filename} thanh cong")
    except FileNotFoundError:
        print(f"Khong tim thay file {filename} ")
        print('Vui long kiem tra lai ten file va khong can nhap dinh dang file')
        sys.exit()

def Encode(text):
    """
    For each character in the text, check if it is in the MorseCode dictionary, and if it is, add the
    corresponding value to the result
    
    :param text: The text to be encoded
    :return: The result of the function is the encoded text.
    """

    result = ""
    for i in text:
        for a, b in MorseCode.items():
            if i.upper() == a:
                result += f"{b} "
    return result 

def Decode(code):
    """
    It takes a string of morse code, splits it into a list, then iterates through the list, and for each
    item in the list, it iterates through the MorseCode dictionary, and if the item in the list is equal
    to the value of the dictionary, it adds the key to the result string
    
    :param code: The string of morse code to be decoded
    :return: The result of the function.
    """

    List = code.split()
    result = ""
    for i in List:
        for a, b in MorseCode.items():
            if i == b:
                result += f"{a}"
    return result


def writeFile(filename, text):
    """
    It opens a file, writes text to it, and then closes it
    
    :param filename: The name of the file you want to write to
    :param text: The text to be written to the file
    """

    f = open(f"{filename}.txt", "a", encoding="utf-8")
    f.write(text)
    f.close()

#Global Environment
inputData = []
text = ""
FileName_Input = input('Nhap ten file muon su dung(khong can nhap dinh dang file .txt): ')
readFile(FileName_Input)
FileName_Output = input('Nhap ten file muon xuat du lieu: ')
text += 'Encode \n========== \n'
for i in inputData:
    EncodeText = Encode(i)
    text += f"{i} : {EncodeText}\n"

text += '\nDecode \n========== \n'

for i in inputData:
    EncodeText = Encode(i)
    DecodeText = Decode(EncodeText)
    text += f"{EncodeText} : {DecodeText}\n"

writeFile(FileName_Output, text)



