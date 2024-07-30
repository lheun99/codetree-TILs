a, b = map(int, input().split())
res = 0
for i in range(a, b+1):
    if (1920 % a == 0 and 2880 % a == 0) or (1920 % b == 0 and 2880 % b == 0):
        res = 1
        break
print(res)