lista =[3,1,2,4,5,0]
def minimum(some_list):
    a = some_list[0]
    for x in range(1, len(some_list)):
        if some_list[x] < a:
            a = some_list[x]
    return a

print('min =',minimum(lista))

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)