n = int(input())
num = ord('A')

for i in range(n):
    for j in range(n):
        print(" " * j, end = " ")

    for z in range(n, 0, -1):
        print(z, end=" ")