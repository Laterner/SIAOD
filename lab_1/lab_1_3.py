import random

#---------------------------------------------------------------
def matrix_generation():
    m = 5
    n = 5
    temp_matrix = []
    for j in range(m):
        temp = []
        for i in range(n):
            temp.append(random.randrange(-1000, 1000))
        temp_matrix.append(temp)
    return temp_matrix


#---------------------------------------------------------------Выборочная
def mode_select(data):
    for temp in data:
        for i in range(0, len(temp) - 1):
            smallest = i
            for j in range(i + 1, len(temp)):
                if temp[j] < temp[smallest]:
                    smallest = j
            temp[i], temp[smallest] = temp[smallest], temp[i]
    return data

#------------------------------------------------------------------Вставка
def mode_insertion(data):
    for temp in data:
        for i in range(len(data)):
            j = i - 1 
            key = temp[i]
            while temp[j] > key and j >= 0:
                temp[j + 1] = temp[j]
                j -= 1
            temp[j + 1] = key
    return data

#------------------------------------------------------------------Обменом
def change_rec(data, i = 0, j = None):
    if j is None:
        j = len(data) - 1
    if data[j] < data[i]:
        data[i], data[j] = data[j], data[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        change_rec(data, i, j - t)
        change_rec(data, i + t, j)
        change_rec(data, i, j - t)
    return data
    
def mode_change(data):
    for temp in data:
        temp = change_rec(temp, 0, len(temp) - 1)
    return data

#--------------------------------------------------------------------Шелла
def mode_shell(data):
    for temp in data:
        inc = len(temp) // 2
        while inc:
            for i, el in enumerate(temp):
                while i >= inc and temp[i - inc] > el:
                    temp[i] = temp[i - inc]
                    i -= inc
                temp[i] = el
            inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data
#----------------------------------------------------------------Турнирная
def mode_turn(data):
    pass

#------------------------------------------------------------------Быстрая
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def mode_quick(data):  
    for temp in data:
        def _quick_sort(items, low, high):
            if low < high:
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(temp, 0, len(temp) - 1)
    return data

#------------------------------------------------------------Пирамидальная
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  
    r = 2 * i + 2   

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап 
        heapify(arr, i, 0)

def mode_pyramid(data):
    for temp in data:
        heapSort(temp)


#--------------------------------------------------------------Точка_входа
if __name__ == "__main__":
    matrix = matrix_generation()

    print("Матрица: ")
    print(matrix)
    print()
    
    print("Сортировка: ")
    print(mode_select(matrix))
    print(mode_insertion(matrix))
    print(mode_change(matrix))
    print(mode_shell(matrix))
    print(mode_turn(matrix))
    print(mode_quick(matrix))
    print(mode_pyramid(matrix))

    

















    