def pyat(mass):
    # table = [[ 1, 2, 3, 4],     #10 + 1 11
    #         [0, 5, 6, 7],       #18 + 2 20
    #         [8, 9, 10, 11],     #48 + 3 51
    #         [12, 13, 14, 15]]   #54 + 4 58
    table = []
    table.append(mass[0:4])
    table.append(mass[4:8])
    table.append(mass[8:12])
    table.append(mass[12:16])

    col = -1
    print(table)
    for i,el in enumerate(table):
        for i in range(len(el) - 1):
            if el[i] > el[i + 1]:
                col += 1
    if col % 2 == 1:
        print("Не решаемая", col)
    else:
        print("Решаемая", col)


def serch_kmp(s, w):
    v = [0]*len(s) # нулевой массив размером len(s)
    n = 0
    k = 0
    
    koko = 0

    while k <= (len(s) - len(w)):
        koko += 1
        for i in range(k, len(s)):
            # print(len(s), len(w), "k:", k, "i:", i, "n:", n, koko)
            if w[i - k] == s[i]:
                n += 1
                v[i] = n
                if n == len(w):
                    # print(v)
                    return i - len(w) + 1
            else:
                n = 0
                v[i] = n
                k = i + 1
                break
            
    # print(v)
    return -1


def forming_d(pattern):
    # Формируем массив d.
    d = [len(pattern) for i in range(256)]
    new_p = pattern[::-1]
 
    for i in range(len(new_p)):
        if d[ord(new_p[i])] != len(new_p):
            continue
        else:
            d[ord(new_p[i])] = i
    return d
 
 
def search_bm(string, pattern):
 
    d = forming_d(pattern)
    # x - начало прохода по string
    # j - проход по pattern
    # k - проход по string
    len_p = x = j = k = len(pattern)
    # число смещений
    counter = 0
 
    while x <= len(string) and j > 0:
        if pattern[j - 1] == string[k - 1]:
            j -= 1
            k -= 1
        else:
            x += d[ord(string[k - 1])]
            k = x
            j = len_p
            counter += 1
 
    if j <= 0:
        return "Нашли. Число смещений равно " + str(counter) + "."
    else:
        return "Не нашли!"
 



if __name__ == "__main__":
    s = "Love is too young to know what conscience is"
    t = "Love is too young to know what conscience is, \
        Yet who knows not conscience is born of love? \
        Then, gentle cheater, urge not my amiss, \
        Lest guilty of my faults thy sweet self prove. \
        For, thou betraying me, I do betray \
        My nobler part to my gross body’s treason: \
        My soul doth tell my body that he may \
        Triumph in love; flesh stays no farther reason; \
        But rising at thy name doth point out thee \
        As his triumphant prize. Proud of this pride, \
        \
        He is contented thy poor drudge to be, \
        To stand in thy affairs, fall by thy side. \
        No want of conscience hold it that I call \
        Her ‘love’ for whose dear love I rise and fall." 

    w = "fall"
    print(serch_kmp(t, w))
    print()

    print("")
    print(search_bm(t, w))
    # pyat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
