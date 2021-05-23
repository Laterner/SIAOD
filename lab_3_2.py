def prefix(s):
    P = [0]*len(s)
    j = 0
    i = 1
    
    while i < len(s):
        if s[j] != s[i]:
            if j > 0:
                j = P[j-1]
            else:           # j == 0
                i += 1
        else:               # s[j] == s[i]
            P[i] = j + 1
            i += 1
            j += 1

    return P

def kmp(sub, s):
    k = 0
    l = 0
    P = prefix(sub)

    while k < len(s):
        if sub[l] == s[k]:
            k += 1
            l += 1

            if l == len(sub):
                return k - len(sub)

        elif l > 0:
            l = P[l-1]
        else:
            k += 1

    return -1


if __name__ == '__main__':
    print(prefix("abbaabbab"))
    s = "abcabeabcabcabd"
    sub = "abcabd"
    lsub = len(sub)
    index = kmp(sub, s)
    print(f"found: {s[index:index+lsub]} index: {index}")

# from PIL import Image
 
# im = Image.open("image.bmp")
# x, y = im.size
 
# for i in range(4):
#     for j in range(4):
#         if i != 4 and j != 4:
#             im.crop((i * (x / 4), j * (y / 4)), ((i + 1) * (x / 4), (j + 1) * (y / 4)))
#             im.save('image{}{}.bmp').format(str(i + 1), str(j + 1))