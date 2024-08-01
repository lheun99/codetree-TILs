n = int(input())

for i in range(1, n+1):
    for j in range(1, n):
        print(f"{i} * {j} = {i*j}", end = " / ")
    print(f"{i} * {n} = {i*n}")
    n -= 1