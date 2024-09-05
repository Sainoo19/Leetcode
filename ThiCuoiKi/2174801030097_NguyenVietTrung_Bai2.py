from random import randint

myBowling = []


def readFile(filename):
    """
    It opens the file, reads each line, replaces the semicolons with commas, and strips the newline
    character from each line
    
    :param filename: the name of the file you want to read
    :return: A list of strings.
    """
    with open(f'{filename}.txt', 'r', encoding='utf-8') as f:#Should use with open as than f = open because contains many subcommand lines inside
        for line in f:
            x = line.replace(';', ',')
            myBowling.append(x.strip('\n')) 
    return myBowling

def playFrame(frameID, playID):
    """
    It takes a frameID and playID as input, and returns a list of the rolls in that frame
    
    :param frameID: The frame number (1-10)
    :param playID: 1 = first roll, 2 = second roll, 3 = third roll
    :return: A list of the rolls for a given frame.
    """
    listScore = []

    if frameID == 9 and playID == 3:
        roll_1 = randint(1,10)
        if roll_1 == 10:#Frame 10 need >= 2 roll
            roll_2 = randint (1,10)
            listScore.append(roll_1)
            listScore.append(roll_2)
            if roll_2 == 10:
                roll_3 = randint(1,10)
            else:
                roll_3 = randint (1, 10 - roll_2)
            listScore.append(roll_3)
        else:
            roll_2 = randint(10 - roll_1 , 10 - roll_1)
            listScore.append(roll_1)
            listScore.append(roll_2)
            if roll_1 + roll_2 == 10:
                roll_3 = randint(1,10)
                listScore.append(roll_3)
    elif frameID == 9 and playID <= 2:#Frame 9 with 1 or 2 roll
        roll_1 = randint(1,8)
        if roll_1 == 8:
            roll_2 = 1
        else:
            roll_2 = randint(1,8 - roll_1)
        listScore.append(roll_1)
        listScore.append(roll_2)
    elif frameID < 9 and playID == 1:#Frame < 9 if have 1 roll => Strike
        roll_1 = 10
        listScore.append(roll_1)
    else:
        roll_1 = randint(1,10)
        if roll_1 == 10:
            listScore.append(roll_1)
        else:
            roll_2 = randint(1, 10 - roll_1)
            listScore.append(roll_1)
            listScore.append(roll_2)
    return listScore
    
def total_score(listname):
    """
    It takes a list of rolls and returns a list of the total score for each frame
    
    :param listname: a list of integers that represent the number of pins knocked down in each roll
    :return: A list of the total score for each frame.
    """
    listTotal = []
    roll_index = 0
    score = 0
    for frame in range(10):
        if Strike(listname, roll_index):
            score += 10 + listname[roll_index+1] + listname[roll_index+2]
            roll_index += 1
            listTotal.append(score)
        elif Spare(listname, roll_index):
            score += 10 + listname[roll_index+2]
            roll_index += 2
            listTotal.append(score)
        else:
            score += listname[roll_index] + listname[roll_index+1]
            roll_index += 2
            listTotal.append(score)
    return listTotal   
        
def Spare(listname, roll_index):
    return listname[roll_index] + listname[roll_index+1] == 10

def Strike(listname, roll_index):
    return listname[roll_index] == 10

listScoreP1 = []
listScoreP2 = []
listScoreP3 = []
Total = []


for frame in range(10):
    print('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print(f'\nFrame {frame+1}\n')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    for i in range(1,4):
        print(f'\nNgười chơi {i}')
        while True:
            try:
                x = int(input('Nhập vào số lần ném: '))
                print('---------------------------')
            except:
                continue
            if frame < 9 and x > 0 and x <= 2:
                break
            if frame == 9 and x > 1 and x <= 3:
                break
        if i == 1:
            listScoreP1 += playFrame(frame,x)
        elif i == 2:
            listScoreP2 += playFrame(frame,x)
        else:
            listScoreP3 += playFrame(frame,x)

Total.append(total_score(listScoreP1))
Total.append(total_score(listScoreP2))
Total.append(total_score(listScoreP3))
FileName_Output = input('Nhap ten file muon xuat du lieu: ')

with open(f'{FileName_Output}.txt', 'w') as f:#Should use with open as than f = open because contains many subcommand lines inside
    for player in range (1,4):
        f.write('{0:6}'.format('BACK'))
        for i in range(1,11):
            f.write(f'\t\t {i}')
        f.write('{0: >30}'.format('FINAL'))
        f.write('\n')

        Score = []
        if player == 1:
            Score = listScoreP1
        elif player == 2:
            Score = listScoreP2
        else:
            Score = listScoreP3
        lan = 0
        f.write('\t   ')
        for i in range(len(Score)):

            if Score[i] == 10:
                f.write('{0: >8}'.format(Score[i]))
            else:
                f.write('{0: >4}'.format(Score[i]))

        finalScore = Total[player-1]

        f.write('\n')

        f.write('{0:8}'.format(' '))
        for i in range(len(finalScore)):
            if finalScore[i] < 10:
                f.write(f'\t|{finalScore[i]}|\t')
            else:
                f.write(f'\t|{finalScore[i]}|')
        f.write('\t\t\t\t[{0: >15}]'.format(finalScore[-1]))
        f.write('\n')
        f.write('\n')
f.close()
readFile('inputBai2')
