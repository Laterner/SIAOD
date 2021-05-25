# -*- coding: utf-8 -*-

from lab_4_0 import *
import os

def _load():
    with open("./authors.txt", encoding='utf-8') as file_handler:
        return [line[:-1] for line in file_handler]
        
def load_deque():
    deque = SelfDeque()
    # authors = _load()
    authors = [4, 3, 5, 2, 3, 15, 2, 34, 5, 0, 1]
    for el in authors:
        deque.pushR(el)
    return deque

def task_1(file):
    with open(file, "r", encoding='utf-8' ) as books:
        books = [book.strip() for book in books]
        print("Не отсортированный дек: \n", books)

        deque_1 = SelfDeque()
        deque_2 = SelfDeque()

        for book in books:
            deque_1.pushR(book)

        while not deque_1.isEmpty():
            x = deque_1.outR()
            deque_1.popR()

            while not deque_2.isEmpty() and deque_2.outR() > x:
                deque_1.pushL(deque_2.outR())
                deque_2.popR()
            deque_2.pushR(x)
        
    return deque_2.deque

def task_2():
    import random
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    random.shuffle(alphabet)
    alphabet = ''.join(alphabet)
    print(alphabet)
    keyRing = SelfDeque()
    for letter in alphabet:
        keyRing.pushR(letter) 

def task_3():
    A = SelfStack()
    B = SelfStack()
    C = SelfStack()

    disks = 9

    for i in range(disks, 0, -1):
        A.push(i)

    def move(a, b):
        if a.size() == 0 and b.size() > 0:
            a.push(b.pop())
        elif a.size() > 0 and b.size() == 0:
            b.push(a.pop())
        elif a.back() > b.back():
            a.push(b.pop())
        else:
            b.push(a.pop())

    if disks % 2 == 0:
        while C.size() != disks:
            move(A, B)
            move(A, C)
            move(B, C)
    else:
        while C.size() != disks:
            move(A, C)
            move(A, B)
            move(C, B)
            move(A, C)
            move(B, A)
            move(B, C)
            move(A, C)

    while not C.isEmpty():
        print(C.pop())


def task_4(string):
    bracket_stack = SelfStack()
    for i in string:
        if i == '(':
            bracket_stack.push(i)
        elif i == ')':
            if bracket_stack.isEmpty():
                return False
            bracket_stack.pop()
    return bracket_stack.isEmpty()

def task_5(string):
    bracket_stack = SelfDeque()
    for i in string:
        if i == '[':
            bracket_stack.pushR(i)
        elif i == ']':
            if bracket_stack.isEmpty():
                return False
            bracket_stack.popR()
    return bracket_stack.isEmpty()

def task_6():
    text = 'Привет от пиксиля-кн20тс! Это послание несёт в себе смысл, или его остутсвие! Не верьте банкам, скупайте носки, любите парки и есшьте сладости.'

    letters = SelfStack()
    digits = SelfStack()
    others = SelfStack()

    for c in text:
        if c.isalpha():
            letters.push(c)
        elif c.isdigit():
            digits.push(c)
        else:
            others.push(c)

    new_text = ''

    letters.stack = letters.stack[::-1]
    digits.stack = digits.stack[::-1]
    others.stack = others.stack[::-1]

    while not digits.isEmpty():
        new_text += digits.pop()

    while not letters.isEmpty():
        new_text += letters.pop()

    while not others.isEmpty():
        new_text += others.pop()

    print(new_text)


def task_8(file):
    with open(file, "r", encoding='utf-8' ) as books:
        stack = SelfStack()
        books = [book.strip() for book in books]

        for book in books:
            stack.push(book)

    with open('task_8.txt', 'w') as filehandle:  
        while not stack.isEmpty():
            filehandle.write('%s\n' % stack.pop())
        return "Fin"


def task_9():
    text = '((T)XF)X(TAT)OT'

    opstack = SelfStack()
    vstack = SelfStack()

    cur = 0
    while True:
        read = False
        if not opstack.isEmpty():
            if opstack.back() == 'N':
                if vstack.isEmpty():
                    read = True
                else:
                    if vstack.pop() == 'T':
                        vstack.push('F')
                    else:
                        vstack.push('T')
                    opstack.pop()
            elif opstack.back() == 'A':
                if vstack.size() < 2:
                    read = True
                else:
                    a = vstack.pop()
                    b = vstack.pop()
                    if a == b and b == 'T':
                        vstack.push('T')
                    else:
                        vstack.push('F')
                    opstack.pop()
            elif opstack.back() == 'O':
                if vstack.size() < 2:
                    read = True
                else:
                    a = vstack.pop()
                    b = vstack.pop()
                    if a == 'T' or b == 'T':
                        vstack.push('T')
                    else:
                        vstack.push('F')
                    opstack.pop()
            elif opstack.back() == 'X':
                if vstack.size() < 2:
                    read = True
                else:
                    a = vstack.pop()
                    b = vstack.pop()
                    if a != b:
                        vstack.push('T')
                    else:
                        vstack.push('F')
                    opstack.pop()
            elif opstack.back() == '(':
                read = True
            elif opstack.back() == ')':
                opstack.pop()
                opstack.pop()
        else:
            read = True
        if read:
            i = text[cur]
            if i in 'FT':
                vstack.push(i)
            if i in 'AXON()':
                opstack.push(i)
            cur += 1
        

        if cur == len(text) and opstack.size() == 0:
            break

    while not vstack.isEmpty():
        print(vstack.pop())

def task_10():
    text = 'N(10, M(4, N(8, (M(6, M(5, 4))))))'

    op = SelfStack()
    nums = SelfStack()

    num = ''

    cur = 0
    while cur < len(text):
        i = text[cur]
        if i.isdigit():
            num += i
        elif num != '':
            nums.push(int(num))
            num = ''
        if i in 'MN':
            op.push(i)
        cur += 1

    while not op.isEmpty():
        a = nums.pop()
        b = nums.pop()
        if a < b:
            a,b = b,a
        if op.pop() == 'M':
            nums.push(a)
        else:
            nums.push(b)

    while not nums.isEmpty():
        print(nums.pop())

def task_11(text):
    stack = SelfStack()

    cur = 0
    while True:
        read = False
        if not stack.isEmpty():
            if stack.back() == '(':
                read = True
            elif stack.back() == ')':
                stack.pop()
                if stack.size() < 2 or stack.pop() != 'formula' or stack.pop() != '(':
                    return False
                stack.push('formula')
            elif stack.back() == 'formula':
                stack.pop()
                if stack.size() > 1 and stack.back() in '+-':
                    if stack.pop() in '+-' and stack.pop() == 'formula':
                        stack.push('formula')
                    else:
                        return False
                else:
                    stack.push('formula')
                    read = True
            else:
                read = True
        else:
            read = True
        if read:
            i = text[cur]
            if i in 'xyz':
                stack.push('formula')
            elif i in '()+-':
                stack.push(i)
            cur += 1
        if cur == len(text) and stack.size() == 1:
            break
    return True

if __name__ == "__main__":
    os.system("cls")
    

    # print("Задание 1")
    # print("Отсортированный дек: \n", task_1("./authors.txt"))

    # print("\nЗадание 3")
    # task_3()

    # print("\nЗадание 4")
    # print(task_4('()())(((()'))
    # print(task_4('(()())()(()())()(()(()(())()))'))

    # print("\nЗадание 5")
    # print(task_5('[][[]['))
    # print(task_5('[[][][][[][][][][[[[]]][[[]]]][]]][]'))

    # print("\nЗадание 6")
    # task_6()

    # print("\nЗадание 8")
    # print(task_8("./authors.txt"))

    # print("\nЗадание 9")
    task_9()

    # print("\nЗадание 10")
    # task_10()

    # print("\nЗадание 11")
    # task_11('((x + y) + (x - y) + z)')
