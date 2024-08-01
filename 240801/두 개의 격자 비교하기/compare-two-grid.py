a, b = map(int, input().split())
num1 = [list(map(int, input().split())) for _ in range(a)]
num2 = [list(map(int, input().split())) for _ in range(a)]

res = [[0 for z in range(b)] for _ in range(a)]

for i in range(a):
    for j in range(b):
        if num1[i][j] != num2[i][j]:
            res[i][j] = 1

for k in range(a):
    for m in range(b):
        print(res[k][m], end = " ")
    print()