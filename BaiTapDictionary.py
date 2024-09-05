
import json

Student_Dict={}

def NhapMau():


    a_dict = {}  
    with open('studentList.txt', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            entry = line.split(' ',1)  
            a_dict[entry[0].strip("' ")] = entry[1].strip()

    print(a_dict)

def AddDict(Dict):
    while True:
        ID = int(input("Enter student's ID: "))
        if ID == -1:
            break
        LastName = input("Enter student's lastName: ")
        MidName = input("Enter student's midName: ")
        FirstName = input("Enter student's firstName: ")

        GPA = int(input("Enter student's GPA: "))
        
        Dict[ID] = LastName,MidName,FirstName,GPA 

    

def MaxGPA(Dict):
    max = 0
    for i in Dict.values():
        if i[-1] > max:
            max = i[-1]
    return max
        

def AVGGPA(Dict,HoSV):
    
    total = 0
    SoPhanTu = 0

    for i in Dict.values():
        if HoSV == i[0]:       
            total += i[-1]
            SoPhanTu += 1
        else:
            ('Khong tim thay ho nay!')

    
    AverageGPA = total/SoPhanTu
    return AverageGPA 

def OutputFile(Dict):
    with open('excellentStudents.txt', 'w') as f:
        for i in Dict.values():
            if i[-1] > 3.2:
                f.write(json.dumps(Dict))
                

def CountDict(Dict,HoSV):
    
    SoPhanTu = 0

    for i in Dict.values():
        if HoSV == i[0]: 
            SoPhanTu += 1
    return SoPhanTu

    
AddDict(Student_Dict)
print(Student_Dict)




print('Max GPA is ',MaxGPA(Student_Dict))
HoSV = input('Nhap ho sinh vien: ')
print('Average GPA is ',AVGGPA(Student_Dict,HoSV))
HoSV = input('Nhap ho sinh vien: ')
print('So sinh vien co ho '+str(HoSV)+' la: ',CountDict(Student_Dict,HoSV))

OutputFile(Student_Dict)
print('---Bonus---')
NhapMau()
