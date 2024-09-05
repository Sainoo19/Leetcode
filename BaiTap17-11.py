def readFile():
    dict = {}
    f = open('input.txt', 'r', encoding='utf-8')
    for line in f:
        xuly1 = line.split()
        if xuly1[0] in dict:
            dict[xuly1[0]] = str(int(xuly1[1]) + int(dict[xuly1[0]]))
        else:
            dict[xuly1[0]] = xuly1[1]
    f.close()
    return dict


def addFruit(name, quantity):
    if name in Fruit:
        while True:
            capnhat = input('Bạn có muốn cập nhật số lượng ?\n')
            if capnhat == 'Có':
                Fruit[name] = str(int(quantity) + int(Fruit[name]))
                break
            elif capnhat == 'Không':
                break
            else:
                print('Vui lòng nhập Có hoặc Không')
    else:
        Fruit[name] = quantity


def findFruit(name):
    if name in Fruit:
        return name + ' has ' + Fruit[name]
    else:
        return 'No has ' + name + ' in Fruit'


def exportFruit(quantity):
    f = open('output.txt','w',encoding='utf-8')
    keys = list(Fruit.keys())
    for i in range(len(keys)):
        if int(Fruit[keys[i]]) > int(quantity):
            f.write(keys[i] + ' - ' + Fruit[keys[i]]+'\n')
    f.close()


Fruit = readFile()
addFruit('Kiwi', '8')
addFruit('Mango', '3')
print(findFruit('Lemon'))
exportFruit(10)

