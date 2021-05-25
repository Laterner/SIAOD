import random

m = 5
n = 5
min_limit = -250
max_limit = 1000 + 22 #(номер своего варианта)

matrix = []
for j in range(m):
    temp = []
    for i in range(n):
        temp.append(random.randrange(min_limit, max_limit + 1))
    matrix.append(temp)

print(matrix)


# n = random.randrange(1, 4)
# min_limit = -250
# max_limit = 1000 + 22 #(номер своего варианта)

# matrix = []
# for j in range(n):
#     matrix.append(random.randrange(min_limit, max_limit))
# print(matrix)
