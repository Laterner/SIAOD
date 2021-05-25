# Задание №1
# Даны две строки: s1 и s2 с одинаковым размером, проверьте,
# может ли некоторая перестановка строки s1 “победить” 
# некоторую перестановку строки s2 или наоборот. 
# Строка x может “победить” строку y (обе имеют размер n), 
# если xi> = yi (в алфавитном порядке) для всех i от 0 до n-1.


def permutation(lst):
    res = []
    _permutation(lst, 0, res)
    return res

def _permutation(lst, i, res):
    if i == len(lst) - 1:
        elem = ''
        for a in lst:
            elem += str(a)
        if elem not in res:
            res.append(elem)
    else:
        for j in range(i, len(lst)):
            swap(lst, i, j)
            _permutation(lst, i + 1, res)
            swap(lst, i, j)

def swap(lst, i, j):
    k = lst[i]
    lst[i] = lst[j]
    lst[j] = k

s1 = input("Введите s1: ")
s2 = input("Введите s2: ")
if len(s1) == len(s2):
    list_s1 = list(s1) 
    list_s2 = list(s2)
    perms_s1 = permutation(list_s1) # перестановка
    perms_s2 = permutation(list_s2)
    res_s1 = [] # ресурс
    res_s2 = []
    for i in perms_s1:
        for j in perms_s2:
            c = True #check
            for k in range(len(s1)):
                if ord(i[k]) < ord(j[k]): # возвращает число из таблицы Unicode
                    c = False
            if c and i not in res_s1:
                res_s1.append(i)
    for i in perms_s2:
        for j in perms_s1:
            c = True
            for k in range(len(s1)):
                if ord(i[k]) < ord(j[k]):
                    c = False
            if c and i not in res_s2:
                res_s2.append(i)
    if len(res_s1) > 0 or len(res_s2) > 0:
        print("true")
    else:
        print("false")
else:
    print("Длины строк не совпадают")

# Задание №2
# Дана строка s, вернуть самую длинную полиндромную подстроку в s.

def reversed(str):  # "переворачивание" строки
    return str[::-1]

string = input("Введите строку: ")
res = ['']
for i in range(len(string)-2):
    for j in range(i+2, len(string)+1):
        if string[i:j] == reversed(string[i:j]):
            if len(string[i:j]) > len(res[0]):
                res = [string[i:j]]
            elif len(string[i:j]) == len(res[0]):
                res.append(string[i:j])
if res[0] == '':
    print("Полиндрома нет")
else:
    print(res)

# Задание №3
# Вернуть количество отдельных непустых подстрок текста, 
# которые могут быть записаны как конкатенация некоторой строки с самой собой 
# (т.е. она может быть записана, как a + a, где a - некоторая строка).

string = input()
res = ['']
for i in range(len(string)-2):
    for j in range(i+2, len(string)+1):
        if (j - i) % 2 == 0:
            center = (i + j) // 2
            if string[i:center] == string[center:j] and string[i:j] not in res:
                if len(string[i:j]) > len(res[0]):
                    res = [string[i:j]]
                elif len(string[i:j]) == len(res[0]):
                    res.append(string[i:j])
if res[0] == '':
    print("Совпадений нет")
else:
    print(res)

# Задание №4: "Треугольник с максимальным периметром"
# Массив A состоит из целых положительных чисел длин отрезков. 
# Составьте из трех отрезков такой треугольник, чтобы его периметр был максимально возможным.
# Если невозможно составить треугольник с положительной площадью функция возвращает 0.


input_a = input("Введите длины отрезков: ")
try:
    a = input_a.split()  # сделан разделенный список длин
    for i in range(len(a)):
        a[i] = int(a[i]) 
    a.sort(reverse = True)
    max_length = 0  # finding a max triangle
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if a[i] < a[j] + a[k]:
                    max_length = max(max_length, a[i] + a[j] + a[k])
    print(max_length)
except ValueError:
    print("Введите корректные данные")

# Задание №5: "Максимальное число"
# Дан массив неотрицательных целых чисел nums. 
# Расположите их в таком порядке, чтобы вместе 
# они образовали максимально возможное число.

input_b = input("Введите числа: ")
def compare(got, cur):
    for i in range(min(len(cur), len(got))):
        if ord(cur[i]) > ord(got[i]):
            return cur
        elif ord(cur[i]) < ord(got[i]):
            return got
        else:
            if i == min(len(cur), len(got)) - 1:
                if len(cur) == len(got):
                    return cur
                if len(got) > len(cur):
                    longer = got
                    shorter = cur
                else:
                    longer = cur
                    shorter = got
                if ord(longer[i + 1]) <= ord(shorter[0]):
                    return shorter
                else:
                    return longer


try:
    b = input_b.split()
    res = ''
    while len(b) > 0:
        c = '0'
        for i in b:
            c = compare(i, c)
        res += c
        b.remove(c)
    if len(res) > 1 and res[0] == '0':
        print("Такого числа не существует")
    else:
        print(res)
except ValueError:
    print("Введите корректные данные")

# Задание №6: "Сортировка диагоналей в матрице"
# Дана матрица mat размером m * n, значения целочисленные. 
# Напишите функцию, сортирующую каждую диагональ матрицы 
# по возрастанию и возвращающую получившуюся матрицу.


mat = [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]
check = True
for i in range(len(mat) - 1):
    if len(mat[i]) != len(mat[i + 1]):
        check = False
        break
if check:
    for i in range(len(mat)):
        array = []
        for j in range(len(mat)):
            if i + j < len(mat):
                array.append(mat[i + j][0 + j])
        array.sort()
        for j in range(len(mat)):
            if i + j < len(mat):
                mat[i + j][0 + j] = array[j]
    for i in range(1, len(mat[0])):
        array = []
        for j in range(len(mat[0])):
            if i + j < len(mat[0]):
                array.append(mat[0 + j][i + j])
        array.sort()
        for j in range(len(mat[0])):
            if i + j < len(mat[0]):
                mat[0 + j][i + j] = array[j]

for i in range(len(mat)):
    print(mat[i])

# Задание №7
# Дан массив отрезков intervals, в котором intervalsi = start_i, end_i, 
# некоторые отрезки могут пересекаться. 
# Напишите функцию, которая объединяет все пересекающиеся отрезки 
# в один и возвращает новый массив непересекающихся отрезков.

intervals = [[1,4],[3,7],[8,11],[20,28]]
def unity(p):
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            if p[j][0] < p[i][0]:
                p[j],p[i] = p[i],p[j] 

    for i in range(len(p)-2):
        if p[i] == p[i+1]:
            p.pop(i+1)

    while True:
        NotChanged = 0
        if len(p) == 1:
            NotChanged = 1
        for i in range(len(p)-1):
            if p[i][1] >= p[i+1][0]:
                p[i+1][0] = p[i][0]
                p[i+1][1] = p[i+1][1]
                p.pop(i) #удаление
                break
            NotChanged = 1
        if NotChanged:
            break
    return p
print(unity(intervals))
print(len(unity(intervals)))

# Задание №8
# На столе стоят 3n стопок монет. Вы и ваши друзья Алиса и Боб забираете стопки монет по следующему алгоритму: 
# 1. Вы выбираете 3 стопки монет из оставшихся на столе. 2. Алиса забирает себе стопку с максимальным количеством монет. 
# 3. Вы забираете одну из двух оставшихся стопок. 4. Боб забирает последнюю стопку. 5. Если еще остались стопки, 
# то действия повторяются с первого шага. Дан массив целых положительных чисел piles. Напишите функцию, 
# возвращающую максимальное число монет, которое вы можете получит

piles =  [6,19,4,10,7,1,5,2,3]

def money(mas):
    if len(mas) % 3 != 0:
        return 'false'
    mas.sort()
    n = len(mas) - 2
    sum = 0
    for i in range(int(len(mas)/3)):
        sum += mas[n]
        n -= 2
    return sum

print(money(piles))  

# Задание №9
# Дан массив points, где pointsi = x_start, x_end. Напишите функцию, 
# возвращающую минимальное количество стрел, которые нужно выпустить, 
# чтобы уничтожить все шарики.


points = [[8,11],[2,6],[1,4],[9,17]]
def Balloons(p):
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            if p[j][0] < p[i][0]:
                p[j],p[i] = p[i],p[j] 
   # print(p)
    for i in range(len(p)-2):
        if p[i] == p[i+1]:
            p.pop(i+1)
   # print(p)
    while True:
        NotChanged = 0
        if len(p) == 1:
            NotChanged = 1
        for i in range(len(p)-1):
            if p[i][1] >= p[i+1][0]:
                p[i+1][0] = p[i+1][0]
                p[i+1][1] = p[i][1]
                p.pop(i) #удаление
                break
            NotChanged = 1
        if NotChanged:
            break
    return p
print(Balloons(points))
print(len(Balloons(points)))


# Вывод
# Были выполнены различные задание и улучшены навыки построения алгоритмов.
