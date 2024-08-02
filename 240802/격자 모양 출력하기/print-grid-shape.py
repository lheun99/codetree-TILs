a, b = map(int, input().split())
arr = [[0 for i in range(a)] for j in range(a)]

for i in range(b):
    n, m = map(int, input().split())

    arr[n-1][m-1] = n*m

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()