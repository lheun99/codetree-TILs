a, b = map(int, input().split())
res = 0
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        res = 1
        break
print(res)