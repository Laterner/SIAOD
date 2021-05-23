# -*- coding: utf-8 -*-
# import antigravity

# from typing import Deque


from lab_4_0 import *
import os

def _load():
    with open("./authors.txt", encoding='utf-8') as file_handler:
        return [line[:-1] for line in file_handler]
        

def mainD():
    deque = SelfDeque()

    word=input("Enter command: ")

    while 'close' not in word:
        if 'isEmpty' in word:
            print(deque.isEmpty())

        elif 'size' in word:
            print(deque.size())

        elif 'popR' in word:
            deque.popR()

        elif 'popL' in word:
            deque.popL()

        elif 'clear' in word:
            deque.clear()

        elif 'pushR' in word:
            a = input()
            while a != '':
                deque.pushR(a)
                a = input()

        elif 'pushL' in word:
            a = input()
            while a != '':
                deque.pushL(a)
                a = input()

        elif 'print' in word:
            print(deque.deque)

        elif 'outR' in word:
            print(deque.outR())

        elif 'outL' in word:
            print(deque.outL())

        else:
            print("Wrong command")
            print()
            
        word = input("Enter command: ")
    print('Bye!')


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



if __name__ == "__main__":
    os.system("cls")
    # mainD()
    print("Задание 1")
    print("Отсортированный дек: \n", task_1("./authors.txt"))

    print("\nЗадание 4")
    print(task_4('()())(((()'))
    print(task_4('(()())()(()())()(()(()(())()))'))

    print("\nЗадание 5")
    print(task_5('[][[]['))
    print(task_5('[[][][][[][][][][[[[]]][[[]]]][]]][]'))

    print("\nЗадание 8")
    print(task_8("./authors.txt"))
