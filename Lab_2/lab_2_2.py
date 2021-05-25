import hashlib

# BinSearch
def BinSearch(li, x):
    i = 0
    j = len(li)-1
    m = int(j/2)
    while li[m] != x and i < j:
        if x > li[m]:
            i = m+1
        else:
            j = m-1
        m = int((i+j)/2)
    if i > j:
        return 'Нет такого'
    else:
        return m

# fiba
def fibbonachi(arr, goal, size):
    fibM2 = 0
    fibM1 = 1
    fibM0 = fibM1 + fibM2

    while (fibM0 < size):
        fibM2 = fibM1
        fibM1 = fibM0
        fibM0 = fibM1+fibM2
    

    offset = -1

    while fibM0 > 1:
        i= min(fibM2+offset, goal-1)

        if arr[i] < goal:
            fibM0 = fibM1
            fibM1 = fibM2
            fibM2 = fibM0-fibM1

        elif arr[i] > goal:
            fibM0 = fibM2
            fibM1 -= fibM2
            fibM2 = fibM0 - fibM1
        else:
            return i

    if fibM1 == 1 and arr[offset+1] == goal:
        return offset + 1

    return -1


def cheack_punch(table, x, y):
    len_d1 = 8 - y

    mas = [0,1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,0]

    if x != y:
        for i in range(len_d1):
            pass
    

def queens():
    table = [
        ['*', '#', '#', '#', '#', '#', '#', '#'], 
        ['#', '#', '#', '#', '#', '#', '#', '#'], 
        ['#', '#', '#', '#', '#', '#', '#', '#'], 
        ['#', '#', '#', '#', '#', '#', '#', '#'], 
        ['#', '#', '#', '#', '#', '#', '#', '#'], 
        ['#', '#', '#', '#', '#', '#', '#', '#'], 
        ['#', '#', '#', '#', '#', '#', '#', '#'], 
        ['#', '#', '#', '#', '#', '#', '#', '#']]
    cheack_punch(table, 0, 0)


def reHash():
    phone_numbers={
        'person1':909090909,
        'person2':808080808,
        'person3':707070707,
        'person4':606060606,
        'person5':505050505,
        'person6':909090901,
        'person7':808080802,
        'person8':707070703,
        'person9':606060604,
        'person10':505050500
    }
    hashMap={
        
    }
    hashMap.update()
    print(phone_numbers.get('person1'))
    
# queens()
if __name__ == "__main__":
    # li = [2,3,4,6,3,1,3,4,5,7,8,9,4,8]
    li = [1,2,3,4,5,6,7,8,9,10]
    
    x = 5
    # print(BinSearch(li, x))
    # print(fibbonachi(li, x, len(li)))
    reHash()
