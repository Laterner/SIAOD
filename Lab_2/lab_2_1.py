import random

def rand(ms):
    tmp = random.randrange(0, 8)
    while tmp in ms:
        tmp = random.randrange(0, 8)
    return tmp


def cheak(table):
    for i in range(8):
        col = 0
        for j in range(8):
            if table[i][j] == "#":
                col += 1
        if col > 1:
            return False

    for i in range(8):
        col = 0
        for j in range(8):
            if table[j][i] == "#":
                col += 1
        if col > 1:
            return False

    return True


def main():
    table = [
        ['*', '*', '*', '*', '*', '*', '*', '*'], 
        ['*', '*', '*', '*', '*', '*', '*', '*'], 
        ['*', '*', '*', '*', '*', '*', '*', '*'], 
        ['*', '*', '*', '*', '*', '*', '*', '*'], 
        ['*', '*', '*', '*', '*', '*', '*', '*'], 
        ['*', '*', '*', '*', '*', '*', '*', '*'], 
        ['*', '*', '*', '*', '*', '*', '*', '*'], 
        ['*', '*', '*', '*', '*', '*', '*', '*']]

    stk = []
    stl = []

    # for i in range(8):
    #     stk.append(rand(stk))
    #     stl.append(rand(stl))

    stk = [2, 0, 5, 6, 7, 3, 1, 4]
    stl = [5, 1, 6, 3, 2, 7, 4, 0]

    print(stk)
    print(stl)

    for i in range(8):
        table[stk[i]][stl[i]] = '#'

    # for i in range(8):
    #     print(table[i])

    if cheak(table):
        print("Good Session")
        for i in range(8):
            print(table[i])
    else:
        print("Bad Session")
    
     


main()
