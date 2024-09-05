import time
import random

def bubble_sort(List):  
    for i in range(0,len(List)-1):  
        for j in range(len(List)-1):  
            if(List[j]>List[j+1]):  
                temp = List[j]  
                List[j] = List[j+1]  
                List[j+1] = temp  
    return List  

def insertion_sort(List): 
        for i in range(1, len(List)):   
            value = List[i]  
            j = i - 1  
            while j >= 0 and value < List[j]:  
                List[j + 1] = List[j]  
                j -= 1  
            List[j + 1] = value  
        return List  

def selection_sort(List):  
    length = len(List)  
      
    for i in range(length-1):  
        minIndex = i  
          
        for j in range(i+1, length):  
            if List[j]<List[minIndex]:  
                minIndex = j  
                  
        List[i], List[minIndex] = List[minIndex], List[i]  
          
          
    return List    


def merge_sort(List):
    if len(List) > 1:


        r = len(List)//2
        L = List[:r]
        M = List[r:]


        merge_sort(L)
        merge_sort(M)

        i = j = k = 0


        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                List[k] = L[i]
                i += 1
            else:
                List[k] = M[j]
                j += 1
            k += 1


        while i < len(L):
            List[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            List[k] = M[j]
            j += 1
            k += 1



def printList(List):
    for i in range(len(List)):
        print(List[i], end=" ")
    print()

def partition(List, low, high):


  pivot = List[high]


  i = low - 1

  for j in range(low, high):
    if List[j] <= pivot:

      i = i + 1


      (List[i], List[j]) = (List[j], List[i])


  (List[i + 1], List[high]) = (List[high], List[i + 1])


  return i + 1


def quick_sort(List, low, high):
  if low < high:

    pi = partition(List, low, high)

    quick_sort(List, low, pi - 1)

    quick_sort(List, pi + 1, high)



def createrandom_list(nx, x, y):
    lx = []
    for j in range(nx):
        randNum = random.randint(x, y)
        if randNum not in lx:
            lx.append(randNum)
    return lx

def TimeRun(sort):
    start_time = time.perf_counter()
    sort(myList)
    print (myList)
    end_time = time.perf_counter()
    
    print(f"Start Time : {start_time}")
    print(f"End Time : {end_time}")
    print(f"Execution Time : {end_time - start_time:0.6f}" )
    
    print()

#global environment
n = 100
a = 1
b = 150

myList = createrandom_list(n, a, b)
print(myList)
print('Bubble sort')
TimeRun(bubble_sort)

print('Insertion sort')
TimeRun(insertion_sort)

print('Selection sort')
TimeRun(selection_sort)

print('Merge sort')
TimeRun(merge_sort)

print('Quick sort')
start_time = time.perf_counter()
size = len(myList)
quick_sort(myList,0, size - 1)
print (myList)
end_time = time.perf_counter()
    
print(f"Start Time : {start_time}")
print(f"End Time : {end_time}")
print(f"Execution Time : {end_time - start_time:0.6f}" )
    
print()





