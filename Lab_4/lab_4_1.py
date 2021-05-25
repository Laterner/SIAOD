
from lab_4_0 import *

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

def mainS():
    stack = SelfStack()

    word=input("Enter command: ")

    while 'exit' not in word:
        if 'size' in word:
            stack.size()
        elif 'pop' in word:
            stack.pop()
        elif 'back' in word:
            stack.back()
        elif 'clear' in word:
            stack.clear()
        elif 'push' in word:
            a = input()
            while a != '':
                stack.push(a)
                a = input()
        elif 'print' in word:
            print(stack.stack)
        else:
            print("Wrong command")
            print()
            
        word = input("Enter command: ")
    print('Bye!')

if __name__ == "__main__":
    mainS()
    mainD()
