
from lab_4_0 import *

if __name__ == "__main__":
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
