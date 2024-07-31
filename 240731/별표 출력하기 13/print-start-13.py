n = int(input())

cnt = 0
for i in range(n, 0, -1):
    print("* " * i)
    cnt += 1
    print("* " * cnt)